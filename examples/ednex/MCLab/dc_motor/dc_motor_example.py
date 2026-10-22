from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.robocar import Robocar


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




robo = Robocar()

def Move(_Direction, _For, _Type, _Speed):
  global Distance_test, initial_ticks, required_ticks, revolutions_required
  if _For == 0:
    return
  if not robo.select_lego:
    robo.select_normal_mode()
  if _Type == "cm":
    import math

    WHEEL_DIAMETER_MM = 60  # Diameter of the wheel in millimeters
    DISTANCE_CM = _For  # Target distance in centimeters
    DISTANCE_MM = DISTANCE_CM * 10  # Convert centimeters to millimeters
    CIRCUMFERENCE_MM = math.pi * WHEEL_DIAMETER_MM  # Wheel circumference in mm

    revolutions_required = DISTANCE_MM / CIRCUMFERENCE_MM

    # Encoder ticks per full revolution (adjust this value based on your encoder specs)
    TICKS_PER_REV = 510

    # Calculate the number of encoder ticks required for the target distance
    required_ticks = revolutions_required * TICKS_PER_REV
  elif _Type == "in":
    import math

    WHEEL_DIAMETER_MM = 60  # Diameter of the wheel in millimeters
    DISTANCE_CM = _For  # Target distance in centimeters
    DISTANCE_in = DISTANCE_CM * 25.4  # Convert centimeters to millimeters
    CIRCUMFERENCE_MM = math.pi * WHEEL_DIAMETER_MM  # Wheel circumference in mm

    revolutions_required = DISTANCE_in / CIRCUMFERENCE_MM

    # Encoder ticks per full revolution (adjust this value based on your encoder specs)
    TICKS_PER_REV = 510

    # Calculate the number of encoder ticks required for the target distance
    required_ticks = revolutions_required * TICKS_PER_REV
  elif _Type == "rotations":
    import math

    # Encoder ticks per full revolution (adjust this value based on your encoder specs)
    TICKS_PER_REV = 535

    # Calculate the number of encoder ticks required for the target distance
    required_ticks = _For * TICKS_PER_REV
  # print("required_ticks", required_ticks)
  initial_ticks = robo.get_encoder_count(2)
  if _Direction == "Forward":
    robo.move_forward(_Speed)
  elif _Direction == "Backward":
    robo.move_backward(_Speed)
  if _Type == "seconds":
    wait(_For)
    robo.move_forward(0)
    wait_ms(10)
  while _Type != "seconds":
    current_ticks = robo.get_encoder_count(2)
    if abs(current_ticks - initial_ticks) >= required_ticks:
      robo.move_forward(0)
      wait_ms(100)
      break
    else:
      wait_ms(1)


robo.init_motor_module()
if not robo.select_lego:
  robo.encoder4.set_all_motors_mode(0x00)
def normal_mode():
  if not robo.select_lego:
    robo.select_normal_mode()
    for i in range(4):
      robo.encoder4.set_motor_pwm_dutycycle(i, 0)

def MotorsStopAll():
  global _Direction, _For, _Type, _Speed, Distance_test, initial_ticks, required_ticks, revolutions_required
  robo.motor_stop(1)
  robo.motor_stop(2)
  robo.motor_stop(3)
  robo.motor_stop(4)

touch_button0 = MCBtn(text='Move CM', x=0, y=116, w=100, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button4 = MCBtn(text='Stop', x=15, y=190, w=70, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
slider0 = MCSlider(x=35, y=82, w=250, h=12, min=0, max=50, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)
label0 = MCLabel('label0', x=126, y=24, color=0x000, font=FONT_MONT_22, parent=None)
touch_button1 = MCBtn(text='Move IN', x=110, y=116, w=100, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button2 = MCBtn(text='Move R', x=220, y=116, w=100, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button3 = MCBtn(text='Move s', x=110, y=180, w=100, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

def touch_button0_pressed():
  # global params
  Move('Forward', (slider0.get_value()), 'cm', 30)
  pass
touch_button0.pressed(touch_button0_pressed)

def touch_button1_pressed():
  # global params
  Move('Forward', (slider0.get_value()), 'in', 30)
  pass
touch_button1.pressed(touch_button1_pressed)

def touch_button2_pressed():
  # global params
  Move('Forward', (slider0.get_value()), 'rotations', 30)
  pass
touch_button2.pressed(touch_button2_pressed)

def touch_button3_pressed():
  # global params
  Move('Forward', (slider0.get_value()), 'seconds', 30)
  pass
touch_button3.pressed(touch_button3_pressed)

def touch_button4_pressed():
  # global params
  MotorsStopAll()
  pass
touch_button4.pressed(touch_button4_pressed)


slider0.set_value(5)
while True:
  label0.set_text(str(slider0.get_value()))
  wait_ms(2)