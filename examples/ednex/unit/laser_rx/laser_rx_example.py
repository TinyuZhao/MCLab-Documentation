from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
laser_rx_0 = unit.get(unit.LASERRX, unit.PORTB)








while True:
  print(laser_rx_0.value())
  wait_ms(2)