# Autonomous Lane Changing‼️
Digital Electronics Final Project, Srikar Punnamaraju
---------------------------------
My final project is a car/tuk-tuk using th Pi-top that can detect its surroundings, which are the front-right/front-left and back-right/back-left of the car, and if there are no objects such as other cars in the way, it will proceed to change langes into the direction that was indicated by the blinker.
- The demo video is linked in `videolink.md` to a Google Drive video
- My digital notebook (for a more detailed and up-to-date log on my project): https://docs.google.com/document/d/1c7jsFXVZwEOZ77Z22pz0kHbZLW0gqdWF3dg5Z6gTTTI/edit?usp=sharing

![final model](https://github.com/svpvip/Autonomous-Lane-Changing/blob/main/final_build.jpg)

Initial Brainstorm
---------------------------------
- I started off the project with brainstorming how I wanted to go about creating my car, and I thought of using ultrasonic sensors to detect the distance, as I was using them and learning how they work prior to starting the project.
- I also wanted to use LEDs to indicate which direction the cars were going, just like car blinkers.
- One thing I was trying to decide was whether I wanted to use Servos to pivot my distance sensor or to have separate sensors at the back, and I decided to go with separate sensors for ease of implementation.

Build
---------------------------------
- The build of the body went through a few different modifications while I was designing my vehicle, and the different iterations/build phases are all in the `build progress` folder.
- I originally used screws on the chassis thinking that it would be easier to modify and layer more components on top of each other, but I soon switched over to the Pi-top studs for ease of maintenance and build time.
- I added protrusions to the side of the chassis on the front and the back for the sensors, and I added a bumper at the front and back for mounting the LEDs. The Pi-top stayed elevated on a platform above other components.
- The lane change button ended up going on the front of the chassis, as that's the place I had the most space left.

Code
---------------------------------
The project's code is all stored in the `final_project.py` and the `code screenshots` folder, use these as a reference for the full code instead of the snippets down here. I imported the required motor functions and the components that were plugged into the ports, and I defined functions for the blinker, such as the `turn_signal_on()` function:
```
def turn_signal_on(choose_led):
  choose_led.on()
  sleep(0.5)
  choose_led.off()
  sleep(0.5)
```
The main logic resides in the `while` loop, where it constantly checks if the turn signal is being pressed down. If it is, then the distance sensors will determine if there is enough space for the car to merge:
```
while True:
  if left_button.is_pressed:
    isPressed = True
    if isPressed:
      if front_sensor.distance <= 0.4 or back_sensor.distance <= 0.4:
        #code to stop the car from merging
        screen.display_text("Too close!")
        turn_signal_off(back_left_led)
        sleep(2.5)
        counter = 0
      else:
        #code that checks if the road stays safe to merge
        screen.display_text("Safe!")
        turn_signal_on(back_left_led)
        counter += 1
        print(counter)
```
Once it is safe to merge, the motors will activate and spin the wheels at different rates to turn the car, one instance shown here:
```
left_motor.set_target_rpm(100)
right_motor.set_target_rpm(-70)
sleep(1.25)
left_motor.set_target_rpm(70)
right_motor.set_target_rpm(-100)
```
Challenges
---------------------------------
- When I was testing with my Pi-top, it would not stay on fore more than a minute or so
- I troubleshooted by changing Pi-tops, the bottom plate, the sensors, as well as the ports
- I switched over to an Ethernet cable when my WiFi connection wasn't working
- I ended up losing a couple days of time due to this, and one way I could have avoided this is by periodically testing and checking if my Pi-top worked so I wouldn't have to make major adjustments at the end

Future Improvements
---------------------------------
- With more time, I would like to have tested out different levels of turning to find the most optimal turn angle for staying in a completely new lane
- I also would have liked to be able to implement all of the sensors that I wanted to use to give the vehicle the capability to merge into the left lane as well
