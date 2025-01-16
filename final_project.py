#required imports
from pitop import Pitop, LED, UltrasonicSensor, Button, EncoderMotor, ForwardDirection, BrakingType
from time import sleep

pitop = Pitop()
screen = pitop.miniscreen

#defining the mencoder motors
left_motor = EncoderMotor("M3", ForwardDirection.CLOCKWISE)
right_motor = EncoderMotor("M0", ForwardDirection.CLOCKWISE)
left_motor.braking_type = BrakingType.BRAKE
right_motor.braking_type = BrakingType.BRAKE

#defining other things that plug into ports
back_left_led = LED("D0")
left_button = Button("D1")
back_sensor = UltrasonicSensor("D2")
front_sensor = UltrasonicSensor("D3")

#functions to control the turn signals blinking or solid
def turn_signal_on(choose_led):
  choose_led.on()
  sleep(0.5)
  choose_led.off()
  sleep(0.5)
  
def manual_control_turn_signal(time, loop, led):
  for i in range(loop):
    led.on()
    sleep(time)
    led.off()
    sleep(time)

def turn_signal_off(choose_led):
  choose_led.on()

#increments whenever the car does not detect anything in the way
counter = 0
isPressed = False

#start of main logic
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
        if counter > 5:
          #merging code
          counter = 0
          screen.display_text("Merging Lanes!")
          left_motor.set_target_rpm(70)
          right_motor.set_target_rpm(-70)
          sleep(1)
          left_motor.set_target_rpm(100)
          right_motor.set_target_rpm(-70)
          sleep(1.25)
          left_motor.set_target_rpm(70)
          right_motor.set_target_rpm(-100)
          sleep(1.25)
          left_motor.set_target_rpm(70)
          right_motor.set_target_rpm(-70)
          sleep(1.5)
          left_motor.stop()
          right_motor.stop()
          turn_signal_off(back_left_led)
          isPressed = False
  else:
    #logic that runs when the turn signal isn't activated
    turn_signal_off(back_left_led)
    screen.display_text("Driving straight!")
