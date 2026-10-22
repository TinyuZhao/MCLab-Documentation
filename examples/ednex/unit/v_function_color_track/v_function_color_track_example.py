from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)


box_detail = None







color_track = V_0.init(V_0.COLOR_TRACK)
while True:
  box_detail = color_track.getBoxDetail(1)
  print((str('Box number: ') + str((color_track.getBoxNumber()))))
  print((str('Box1 pixels changed: ') + str(box_detail[0])))
  print((str('Box1 x: ') + str(box_detail[1])))
  print((str('Box1 y: ') + str(box_detail[2])))
  print((str('Box1 w: ') + str(box_detail[3])))
  print((str('Box1 h: ') + str(box_detail[4])))
  wait_ms(2)
