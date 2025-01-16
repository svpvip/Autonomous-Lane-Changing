# Autonomous Lane Changing‼️‼️‼️
Digital Electronics Final Project, Srikar Punnamaraju
---------------------------------
My final project is a car/tuk-tuk using th Pi-top that can detect its surroundings, which are the front-right/front-left and back-right/back-left of the car, and if there are no objects such as other cars in the way, it will proceed to change langes into the direction that was indicated by the blinker.

![final model](https://github.com/svpvip/Autonomous-Lane-Changing/blob/main/final_build.jpg)

Initial Brainstorm
---------------------------------
I started off the project with brainstorming how I wanted to go about creating my car, and I thought of using ultrasonic sensors to detect the distance, as I was using them snd learning how they work prior to starting the project. I also wanted to use LEDs to indicate which direction the cars were going, just like car blinkers. One thing I was trying to decide was whether I wanted to use Servos to pivot my distance sensor or to have separate sensors at the back, and I decided to go with separate sensors for ease of implementation.

Build
---------------------------------
The build of the body went through a few different modifications while I was designing my vehicle, and the different iterations/build phases are all in the `build progress` folder. I originally used screws on the chassis thinking that it would be easier to modify and layer more components on top of each other, but I soon switched over to the Pi-top studs for ease of maintenance and build time. I added protrusions to the side of the chassis on the front and the back for the sensors, and I added a bumper at the front and back for mounting the LEDs. The Pi-top stayed elevated on a platform above other components. The lane change button ended up going on the front of the chassis, as that's the place I had the most space left.

Code
---------------------------------
The project's code is all stored in the `final_project.py` and the `code screenshots` folder. I imported the required motor functions and the components that were plugged into the ports, and I defined functions for the blinker, such as the `turn_signal_on()` function:
```

```
