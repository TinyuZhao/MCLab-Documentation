from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_tools import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




unitv_base = UnitVBase()
color_detect = ColorDetect(unitv_base)

label0 = MCLabel('label0', x=0, y=113, color=0x000000, font=FONT_MONT_14, parent=None)




color_detect.init()
while True:
  result = color_detect.get_discover_color()
  label0.set_text(str(result))
  print(result)
  wait_ms(2)
