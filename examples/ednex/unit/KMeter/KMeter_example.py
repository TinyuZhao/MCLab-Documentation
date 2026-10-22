from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
KMeter_0 = unit.get(unit.KMETER, unit.PORTA)








KMeter_0.init_i2c_address(0x66)
while True:
  print(KMeter_0.get_kmeter(1))
  print(KMeter_0.get_kmeter(2))
  wait_ms(2)