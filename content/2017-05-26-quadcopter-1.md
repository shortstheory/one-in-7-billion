title: Time Optimisation
date: 2017-05-26 09:30
author: Arnav Dhamija
tags: Electronics, Quadcopters
category: Article
slug: quadcopter-1
status: draft

I've been gravitating more towards working on electronics projects. It's a nice change from pecking the keyboard all day and it has plenty of interesting challenges of its own. The biggest difference I found is that you just can't take your hardware working correctly for granted. Things break, crash, smoke, and burn all too easily if you're not careful with what you're doing.

The idea is to take a quadcopter and give it *some* ability to navigate unsupervised. This approach is (aptly?) called Simultaneous Localisation and Mapping, or SLAM. SLAM is by no means a cheap affair, be it in terms of hardware or software complexity. Using SLAM outdoors normally requires some kind of 3D localiser (such as a depth camera or LIDAR), GPS, and a fairly beefy computer to map the environment.

Of course, I'm setting my expectations low, and I will be more than happy if I can get something out of this which is 10% as good as flying a quadcopter by hand.

It all begins with the hardware and I'm going with this parts list:

* 4-axis 450mm Glass Fiber Frame
* 1045 Propellors x4
* REES52 CC3D F1 Flight computer
* REES52 1000KV A2212 30A Brushless Motor x4
* REES52 SimonK 30A Electronic Speed Controllers
* SunRobotics 2200mAh 3S 35C LiPo Battery

The amount of components embedded in these parts is astounding. Each motor is driven by an ESC, which is essentially a full-fledged 8-bit SoC. The CC3D is an engineering marvel in it's own right - it comes with a 32-bit, 72MHz microcontroller, an MPU6000 for the IMU, and has expansion ports for GPS and Telemetry data.

What I'm interested in, however, is controlling the CC3D in real-time using an Arduino. Typically, the CC3D is linked to a radio receiver which outputs a PWM to six different channels for controlling the quadcopter. 
