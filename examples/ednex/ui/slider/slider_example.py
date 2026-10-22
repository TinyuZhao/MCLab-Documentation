from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


value = None



slider0 = MCSlider(x=60, y=114, w=200, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)



def slider0_changed(value):
  print(slider0.get_value())
  pass
slider0.changed(slider0_changed)


