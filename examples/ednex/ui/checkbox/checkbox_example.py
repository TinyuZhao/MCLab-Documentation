from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






checkbox0 = MCCheckbox(text='checkbox0', x=88, y=109, text_c=0x000, check_c=0x000, font=FONT_MONT_18, parent=None)

def checkbox0_checked():
  # global params
  print('box checked')
  pass
checkbox0.checked(checkbox0_checked)

def checkbox0_unchecked():
  # global params
  print('box unchecked')
  pass
checkbox0.unchecked(checkbox0_unchecked)

