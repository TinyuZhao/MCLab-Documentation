from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
thermal_0 = unit.get(unit.THERMAL, unit.PORTA)








thermal_0.set_refresh_rate(0b001)
while True:
  thermal_0.update_temperature()
  print(thermal_0.get_center_temperature())
  wait_ms(2)