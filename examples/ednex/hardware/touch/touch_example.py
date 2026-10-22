from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MakerAndCoder import touch


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








while True:
  if touch.status():
    print(touch.read())
  wait_ms(2)