from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
encoder_0 = unit.get(unit.ENCODER_LED, unit.PORTA)








encoder_0.set_LED_RGB(3, 0xff0000)
while True:
  print(encoder_0.get_encoder_count())
  print(encoder_0.get_button_status())
  wait_ms(50)
  wait_ms(2)