from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
tvoc_0 = unit.get(unit.TVOC, unit.PORTA)








while True:
  print((str('IAP baseline: ') + str((tvoc_0.get_iaq_baseline()))))
  print((str('TVOC now') + str((tvoc_0.TVOC))))
  print((str('eCO2 now') + str((tvoc_0.eCO2))))
  print((str('H2 now') + str((tvoc_0.H2))))
  print((str('Ethanol now') + str((tvoc_0.Ethanol))))
  wait(0.5)
  wait_ms(2)