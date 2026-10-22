from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.gyro_imu import Gyro
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




gyro = Gyro()

label0 = MCLabel('label0', x=24, y=35, color=0x000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=26, y=90, color=0x000, font=FONT_MONT_14, parent=None)
label2 = MCLabel('label2', x=25, y=137, color=0x000, font=FONT_MONT_14, parent=None)
label3 = MCLabel('label3', x=24, y=175, color=0x000, font=FONT_MONT_14, parent=None)


gyro.init()
while True:
  label0.set_text(str(gyro.get_accel(0)[0]))
  label1.set_text(str(gyro.get_accel(1)[0]))
  label2.set_text(str(gyro.get_gyro(0)[0]))
  label3.set_text(str(gyro.get_gyro(1)[0]))
  wait_ms(20)
  wait_ms(2)