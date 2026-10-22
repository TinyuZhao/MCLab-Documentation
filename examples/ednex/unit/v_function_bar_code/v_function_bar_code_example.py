from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)








bar = V_0.init(V_0.BARCODE)
while True:
  print((str('Code text: ') + str((bar.getBARcodeText()))))
  print((str('Code type: ') + str((bar.getBARcodeRotation()))))
  print((str('Code rotation: ') + str((bar.getBARcodeType()))))
  print((str('Code location: ') + str((bar.getBARcodeLocation()))))
  wait_ms(2)