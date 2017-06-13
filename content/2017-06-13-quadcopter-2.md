title: Quadcopters - Some DIY
date: 2017-06-13 09:30
author: Arnav Dhamija
tags: Electronics, Quadcopters
category: Article
slug: quadcopter-2
status: draft

We have liftoff!

The quadcopter has been built! I had some problems during the building process, so this is a guide which will hopefully make things easier for people to start off with making their own quadcopters.

I suggest going through all these websites before purchasing a single part for your quadcopter. It's not an extensive list, so I'll keep updating it as I find more useful links:

* [OscarLiang](http://oscarliang.com/)
* [Propwashed](www.propwashed.com/)

For clarity, the components I have used in my build are:

* 1045 Propellers x4
* REES52 DJI F450 Frame
* REES52 CC3D F1 Flight Computer
* REES52 1000KV A2212 30A Brushless Motor x4
* REES52 SimonK 30A Electronic Speed Controllers x4
* SunRobotics 2200mAh 3S 35C LiPo Battery
* FlySky FSCT6B Computer Transmitter

Most of these parts can be picked straight off Amazon. REES52 has a good bundle for a pair of propellers, 1000 KV motor, and ESC which I would recommend buying to keep costs low.

The first thing you would want to do is start off with the frame of the quadcopter. If you go for a DJI F450 frame (or one of its hundred clones), you will get a box with four arms (technically called booms) for mounting the motors and ESCs, a base which doubles as a power distribution board, and a board to hold the top of the copter together. It's pretty simple to set up and all you need is two Allen keys to screw everything together.

Once you've setup the frame, the next thing you should do is take a look at the motors. These motors are [brushless](https://en.wikipedia.org/wiki/Brushless_DC_electric_motor) [motors](http://electronics.howstuffworks.com/brushless-motor.htm) and they are very different from brush motors. For starters they have three leads. Another pecularity about these motors are that they are outrunner motors. This means that the case of the motor rotates with the propeller and not the motor shaft alone.

<insert motor image>

These motors can generate a great deal of heat when running at full power. I would *not* recommend testing it at full power on the ground as there won't be any airflow to cool the motor down. This can permenantly damage your motor, and if you're unlucky, your ESC as well.

Anyway, the motors can be screwed directly into the booms of the quadcopter. The direction of rotation is determined by the ESC, so we don't need to worry about that at the moment.

After this, mount the ESCs on to the booms with rubber bands, or better, zip-ties. The ESCs regulate the amount of power going to the motor depending on throttle input and can get very hot as well. Mounting the ESCs under the booms will give it sufficient airflow to cool down properly. You want to make sure that the three wires with female bullet connectors is facing the male bullet connectors of the motor. The other side with the male connector and the BEC goes to the power distribution board of the quadcopter.

As with all electronics with large capactiors, ESCs can have spectacular explosions when things go wrong. Short circuits or using the wrong polarity on the power input side of the ESC can cause it to get damaged in the matter of seconds.

On the other hand, things are a lot more flexible on the power output side of the ESC. *Apparently*, it is possible to connect the three output connectors in any order to the motor, but a good rule of thumb is to connect the middle wire of the ESC to the ground wire of the motor and to interchange the other two wires to reverse the direction of rotation.

<insert ESC image>

Now for the good stuff, go ahead and mount the CC3D on the top frame of the quadcopter. Most CC3D's will come with some plastic adapters and a sticky sheet to stick the CC3D on the quadcopter frame. Take note of the arrow on the CC3D and make sure it is facing the direction in which you want your quadcopter to fly forward. Make sure you leave enough room for keeping the mini USB port and the servo header pins accessible!

After [binding](http://helihelp.rabbitsvc.com/BindingTheTransmitter.aspx) the transmitter to the receiver, plug it into the receiver port of the CC3D. If you use the FlySky CT6B transmitter/receiver, the receiver probably won't work when directly connected to the CC3D on USB power. If so, you can use an Arduino's 5V and GND to power the receiver for testing it. When flying the quadcopter on Li-Po power, the CC3D will be powered by the ESC BEC's which will give it enough headroom to power the receiver.

The final step is
