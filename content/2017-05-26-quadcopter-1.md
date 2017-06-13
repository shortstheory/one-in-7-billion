title: Quadcopters - The Beginning!
date: 2017-05-26 09:30
author: Arnav Dhamija
tags: Electronics, Quadcopters
category: Article
slug: quadcopter-1

I've been gravitating more towards working on electronics projects. It's a nice change from pecking the keyboard all day and it has plenty of interesting challenges of its own. The biggest difference I found is that you just can't take your hardware working correctly for granted. Things break and catch fire all too easily if you're not careful with what you're doing.

My plan is to make a quadcopter from scratch (a rather loose term) and give it *some* ability to navigate unsupervised. This approach is (aptly?) called Simultaneous Localisation and Mapping, or SLAM. SLAM is by no means a cheap affair, be it in terms of hardware or software complexity. Using SLAM outdoors normally requires some kind of 3D localiser (such as a depth camera or LIDAR), GPS, and a fairly beefy computer to map the environment.

Of course, I'm setting my expectations low, and I will be very happy if I can get something out of this which is 10% as good as a human flying quadcopter by hand.

It all begins with the hardware and I'm going with this parts list:

* REES52 DJI F450 Frame
* 1045 Propellers x4
* REES52 CC3D F1 Flight Computer
* REES52 1000KV A2212 30A Brushless Motor x4
* REES52 SimonK 30A Electronic Speed Controllers
* SunRobotics 2200mAh 3S 35C LiPo Battery
* FlySky FSCT6B Computer Transmitter

The amount of embedded systems tech in these components is astounding. Each motor is driven by an ESC, which is essentially a full-fledged 8-bit SoC. The CC3D Flight Computer is an engineering marvel in it's own right - it comes with a 32-bit/72MHz flashable microcontroller, an MPU6000 gyroscope/accelerometer for the IMU, and has expansion ports for GPS and Telemetry data. Even the battery is remarkable - it's capable of discharging 850W at peak performance.

What I'm interested in, however, is controlling the CC3D in real-time using an Arduino. Typically, the CC3D is connected to a radio receiver which is wirelessly linked to a transmitter remote which is controlled by hand. The reciever is interfaced to the CC3D by outputting a PWM to each of the 6 channels when the transmitter is operated. Each channel is usually dedicated to only one axis of movement. For example, there are four dedicated channels for throttle control, yaw, roll, and pitch.

The idea behind this is that one day, I will have a lightweight computer (anyone willing to donate an NUC?) on the quadcopter doing SLAM in real-time. The computer will send throttle, pitch, yaw, and roll commands to the Arduino. The Arduino in turn will feed the CC3D with control signals to execute the maneouver plan. It all may seem like a Rube Goldberg machine, but it's a lot easier than building my own flight computer to do the same.

To kick things off, I had to find the PWM frequency the receiver uses for controlling the ESC. To do this, I connected a pin from the output channel of the receiver to an ad-hoc [Arduino Leonardo oscilloscope](http://www.instructables.com/id/Arduino-Oscilloscope-poor-mans-Oscilloscope/). Using the Processing library, we can get a 0-5V reading of the value on the A0 analog input of the Arduino.

![]({filename}/images/quadcopter/Capture2.PNG)

Not a bad start! The peaks are a pretty clear sign that it's a PWM with a low duty cycle. Using a ruler and some more code, I found that the peak to peak time is about 20ms, which works out to be a PWM frequency of 50Hz. This is in line with some websites speculating it works similarly to a servo control.

The length of time at the peak gives us the signal we need to send using the Arduino. Using some more analysis of the waveform, it looked like the signal were about 1-2ms long. A bit more research yielded that this is very similar to the waveform used for controlling servos. Fortunately, the Arduino has a Servo library meant just for this purpose. Using the writeMicroseconds() function, I got a pretty similar waveform:

![]({filename}/images/quadcopter/Capture7.PNG)

I would go as far to say that this is an even *cleaner* signal than what the reciever outputs. I needed a 5V->3.3V voltage divider for the output, so I used 3 identical resistors in series to do the job.

Next thing was to get the CC3D to accept the input. For this it requires **manual** calibration of the transmitter. In Librepilot, the procedure is quite straightforward - you need to shift the sticks through their minimum, maximum, and neutral outputs to calibrate the CC3D for your transmitter. To do this, I mounted a push button on the Arduino which would cycle through 3 states each time it is pressed - 1100uS, 1500uS, and 1900uS. Not very elegant. Then again, if it's stupid but works, it ain't stupid.

I will be building the rest of the quadcopter once the parts arrive. You can find the code for the Arduino part here: [https://github.com/shortstheory/quadcopter-experiments/blob/master/tristate.ino](https://github.com/shortstheory/quadcopter-experiments/blob/master/tristate.ino)
