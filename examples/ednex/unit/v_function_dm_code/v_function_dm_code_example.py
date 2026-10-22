from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)








dm = V_0.init(V_0.DATAMATRIX)
while True:
  print((str('DM code rotation: ') + str((dm.getDMcodeRotation()))))
  print((str('DM code location: ') + str((dm.getDMcodeLocation()))))
  print((str('DM code text: ') + str((dm.getDMcodeText()))))
  wait_ms(2)