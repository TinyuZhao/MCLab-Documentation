from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from servo import Servo
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








servo0 = Servo(26,50,500,2500,180)
while True:
  servo0.write_angle(0)
  wait(1)
  servo0.write_angle(180)
  wait(1)
  servo0.write_us(500)
  wait(1)
  servo0.write_us(2500)
  wait(1)
  wait_ms(2)