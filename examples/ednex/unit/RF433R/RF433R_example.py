from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
RF433R_0 = unit.get(unit.RF433RX, unit.PORTB)








RF433R_0.start_receiver()
RF433R_0.clear_buffer()
while True:
  if RF433R_0.rx_len:
    print(RF433R_0.rx_buf)
  wait(1)
  wait_ms(2)