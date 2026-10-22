from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_tools import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


result = None

unitv_base = UnitVBase()
color_track = ColorTrack(unitv_base)

label0 = MCLabel('label0', x=0, y=113, color=0x000000, font=FONT_MONT_14, parent=None)




color_track.init()
color_track.set_track_color(0, 100, (-20), 20, (-100), (-20))
while True:
  print(color_track.get_color_box_number())
  if (color_track.get_color_box_number()) > 0:
    result = color_track.get_color_box_detials(0)
  else:
    result = 'Not find blue color'
  label0.set_text(str(result))
  print(result)
  wait_ms(2)
