from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
Watering_0 = unit.get(unit.WATERING, unit.PORTB)








while True:
  print((str('Water: ') + str((Watering_0.get_adc_value()))))
  if (Watering_0.get_adc_value()) < 1000:
    Watering_0.set_pump_status(1)
  else:
    Watering_0.set_pump_status(0)
  wait(0.3)
  wait_ms(2)