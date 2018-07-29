title: GSoC 2018 - Batteries Included!
date: 2018-07-22 22:30
author: Arnav Dhamija
tags: Ardupilot, GSoC, Programming
category: Article
slug: ardupilot-gsoc-update
sidebarimage: ../images/qcside.jpg

Much time has passed and much code has been written since my last update. Adaptive Streaming (a better name TBD) for Ardupilot is nearly complete and brings a whole slew of features useful for streaming video from cameras on robots to laptops, phones, and tablets:

* Automatic quality selection based on bandwidth and packet loss estimates
* Options to record the live-streamed video feed to the companion computer (experimental!)
* Fine tuned control over resolution and framerates
* Multiple camera support over RTSP
* Hardware-accelerated H.264 encoding for supported cameras and GPUs
* Camera settings configurable through the APWeb GUI

Phew!

The configuration required to get everything working is minimal once the required dependencies have been installed. This is in no small part possible thanks to the GStreamer API which took care of several low level complexities of live streaming video over the air.

Streaming video from aerial robots is probably the most difficult use case of Adaptive Streaming as the WiFi link is very flaky at these high speeds and distances. I've optimised the project around my testing with video streaming from quadcopters so the benefits are passed on to streaming from other robots as well.

## Algorithm

I've used a simplification of TCP's [congestion control](https://en.wikipedia.org/wiki/TCP_congestion_control) algorithm for Adaptive Streaming. I had looked at other interesting approaches including estimating receiver [buffer occupancy](https://www.researchgate.net/publication/280738389_An_Analysis_of_TCP-Tolerant_Real-Time_Multimedia_Distribution_in_Heterogeneous_Networks?_sg=pcxT2q90osdkY06gupLQqwssRN0DZrsL3zP2oyqKVIjTML5RhEIWWX5S3-N4KbDRVqHbTc3i2VNzBBpVuQ72t9iSWyT10_8i6w), but using this approach didn't yield significantly better results. TCP's congestion control algorithm avoids packet loss by mandating ACKs for each successfully delivered packet and steadily increasing sender bandwidth till it reaches a dynamically threshold.

A crucial difference for Adaptive Streaming is that 1) we stream over UDP for lower overhead (so no automatic TCP ACKs here!) 2) H.264 live video streaming is fairly loss tolerant so it's okay to lose some packets instead of re-transmitting them. 

Video packets are streamed over dedicated RTP packets and Quality of Service (QoS) reports are sent over RTCP packets. These QoS reports give us all sorts of useful information, but we're mostly interested in seeing the number of packets loss between RTCP transmissions.

On receiving a RTCP packet indicating any packet loss, we immediately shift to a Congested State (better name pending) which significantly reduces the rate at which video streaming bandwidth is increased on receiving a lossless RTCP packet. The encoding H.264 encoding bitrate is limited to no higher than 1000kbps in this state. 

Once we've received five lossless RTCP packets, we shift to a Steady State which can encode upto 6000kbps. In this state we also increase the encoding bitrate at a faster rate than we do in the Congested State. A nifty part of dynamically changing H.264 bitrates is that we can also seamlessly switch the streamed resolution according to the available bandwidth, just like YouTube does with DASH!

This algorithm is fairly simple and wasn't too difficult to implement once I had figured out all the GStreamer plumbing for extracting packets from buffers. With more testing, I would like to add long-term bitrate adaptations for the bitrate selection algorithm.

## H.264 Encoding

This is where we get into the complicated and wonderful world of video compression algorithms.

Compression algorithms are used in all kinds of media, such as JPEG for still images and MP3 for audio. H.264 is one of several compression algorithms available for video. H.264 takes advantage of the fact that a lot of the information in video between frames is redundant. so instead of saving 30 frames for 1 second of 30fps video, it saves one entire frame (known as the Key Frame or I-Frame) of video and computes and stores only the differences in frames with respect to the keyframe for the subsequent 29 frames. H.264 also applies some logic to _predict_ future frames to further reduce the file size. 

This is by no means close to a complete explanation of how H.264 works, for further reading I suggest checking out Sid Bala's [explanation](https://sidbala.com/h-264-is-magic/) on the topic.

The legendary Tom Scott also has a fun [video explaining how H.264 is adversely affected by snow and confetti](https://www.youtube.com/watch?v=r6Rp-uo6HmI)!

https://www.youtube.com/watch?v=r6Rp-uo6HmI

The frequency of capturing keyframes can be set by changing the encoder parameters. In the context of live video streaming over unstable links such as WiFi, this is very important as packet loss can cause keyframes to be dropped. Dropped keyframes severely impact the quality of the video until a new keyframe is received. This is because all the frames transmitted after the keyframe only store the differences with respect to the keyframe and do not actually store a full picture on their own.

Increasing the keyframe interval means we send a large, full frame less frequently, but also means we would suffer from terrible video quality for an extended period of time on losing a keyframe. On the other hand, shorter keyframe intervals can lead to a wastage of bandwidth.

I found that a keyframe interval of every 10 frames worked much better than the default interval of 60 frames without impacting bandwidth usage too significantly.

Lastly, H.264 video encoding is a very computationally expensive algorithm. Software-based implementations of H.264 such as ```x264enc``` are well supported with several configurable parameters but have prohibitively high CPU requirements, making it all but impossible to livestream H.264 encoded video from low power embedded systems. Fortunately, the Raspberry Pi's Broadcom BCM2837 SoC has a dedicated H.264 hardware encoder pipeline for the Raspberry Pi camera which drastically reduces the CPU load in high definition H.264 encoding. Some webcams such as the Logitech C920 and higher have onboard H.264 hardware encoding thanks to special ASIC's dedicated for this purpose. 

Adaptive Streaming probes for the type of encoding supported by the webcam and whether it has the IOCTL's required for changing the encoding parameters on-the-fly.

H.264 has been superseded by the more efficient H.265 encoding algorithm, but the CPU requirements for H.265 are even higher and it doesn't enjoy the same hardware support as H.264 does for the time being.

## GUI

The project is soon-to-be integrated with the APWeb project for configuring companion computers. Adaptive Streaming works by creating an RTSP Streaming server running as a daemon process. The APWeb process connects to this daemon service over a local socket to populate the list of cameras, RTSP mount points, and available resolutions of each camera.

![]({filename}/images/apweb-screenshot.png)

The GUI is open for improvement and I would love feedback on how to make it easier to use!

Once the RTSP mount points are generated, one can livestream the video feed by entering in the RTSP URL of the camera into VLC. This works on all devices supporting VLC. However, VLC does add two seconds of latency to the livestream for reducing the jitter. I wasn't able to find a way to configure this in VLC, so an alternative way to get a lower latency stream is by using the following ```gst-launch``` command in a terminal:

```gst-launch-1.0 playbin uri=<RTSP Mount Point> latency=100```

In the scope of the GSoC timeline, I'm looking to wind down the project by working on documentation, testing, and reducing the cruft from the codebase. I'm looking forward to integrating this with companion repository soon!

Links to the code:

https://github.com/shortstheory/adaptive-streaming
https://github.com/shortstheory/APWeb