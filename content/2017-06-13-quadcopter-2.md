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

The first thing you would want to do is start off with the frame of the quadcopter. If you go for a DJI F450 frame (or one of its hundred clones), you will get a box with four arms (technically called booms) for mounting the motors and ESCs, a base which doubles as a power distribution board, and a board to hold the top of the copter together. It's pretty simple to set up and all you need is two Allen keys to screw everything together.

Once you've setup the frame, the next thing you should do is take a look at the motors. These motors are [brushless](https://en.wikipedia.org/wiki/Brushless_DC_electric_motor) [motors](http://electronics.howstuffworks.com/brushless-motor.htm) and they are very different from brush motors. For starters they have three leads. Another pecularity about these motors are that they are outrunner motors. This means that the case of the motor rotates with the propeller and not the motor shaft alone.

<insert motor image>

These motors can generate a great deal of heat when running at full power. I would *not* recommend testing it at full power on the ground as there won't be any airflow to cool the motor down. This can permenantly damage your motor, and if you're unlucky, your ESC as well.

Anyway, the motors can be screwed directly into the booms of the quadcopter. The chirality is determined by the ESC, so we don't need to worry about that at the moment.

After this, mount the ESCs on to the booms with rubber bands, or better, zip-ties. The ESCs regulate the amount of power going to the motor and can get very hot as well. Mounting the ESCs under the booms will give it sufficient airflow to cool properly. You want to make sure that the three wires with female bullet connectors is facing the male bullet connectors of the motor. The other side with the male connector and the BEC goes to the power distribution board of the quadcopter.

As with all electronics with large capactiors, ESCs can have spectacular explosions when things go wrong. Short circuits or using the wrong polarity on the power input side of the ESC can cause it to get damaged in the matter of seconds.
