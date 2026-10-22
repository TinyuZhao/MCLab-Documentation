from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
servos8_0 = unit.get(unit.SERVOS8, unit.PORTA)








servos8_0.init_i2c_address(0x25)
servos8_0.set_config_mode(0, 0)
print(servos8_0.get_config_mode(0))
while True:
  print(servos8_0.read_input_pin(0))
  wait(1)
  wait_ms(2)