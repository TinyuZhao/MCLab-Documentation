from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
pbhub_0 = unit.get(unit.PBHUB, unit.PORTA)






label0 = MCLabel('label0', x=119, y=101, color=0x000000, font=FONT_MONT_14, parent=None)


pbhub_0.setBrightness(2, 100)
pbhub_0.setColor(2, 0, 3, 0xff0000)
while True:
  pbhub_0.setServoAngle(0, 0, 90)
  wait(1)
  pbhub_0.setServoAngle(0, 0, 0)
  wait(1)
  wait_ms(2)