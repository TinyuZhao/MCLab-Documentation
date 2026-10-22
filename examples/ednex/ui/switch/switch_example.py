from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






switch1 = MCSwitch(x=156, y=104, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)

def switch0_on():
  # global params
  print('switch on')
  pass
switch0.on(switch0_on)

def switch0_off():
  # global params
  print('switch off')
  pass
switch0.off(switch0_off)


switch0.set_bg_color(0xccffff)
switch0.set_color(0x33ff33)