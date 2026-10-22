from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






touch_button0 = MCBtn(text='button0', x=106, y=105, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

def touch_button0_pressed():
  # global params
  print('touch button was pressed')
  pass
touch_button0.pressed(touch_button0_pressed)

