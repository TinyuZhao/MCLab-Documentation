from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)








line_tracker = V_0.init(V_0.LINE_TRACKER)
while True:
  print((str('Line angle') + str((line_tracker.getAngle()))))
  wait_ms(2)