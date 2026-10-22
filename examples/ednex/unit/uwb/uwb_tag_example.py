from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
uwb_0 = unit.get(unit.UWB, unit.PORTC)








uwb_0.init_uwb_mode()
uwb_0.set_mode()
while True:
  if uwb_0.check_device:
    print((str('distance') + str((uwb_0.get_distance_measure[0]))))
  wait_ms(2)