from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
KMeterISO_0 = unit.get(unit.KMETER_ISO, unit.PORTA)








KMeterISO_0.init_i2c_address(0x66)
while True:
  if KMeterISO_0.get_isready():
    print(KMeterISO_0.get_kmeter_thermo(1))
    print(KMeterISO_0.get_kmeter_internal(1))
  wait(1)
  wait_ms(2)