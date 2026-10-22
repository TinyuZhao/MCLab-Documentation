from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
laser_tx_0 = unit.get(unit.LASERTX, unit.PORTB)








while True:
  if btnA.wasPressed():
    laser_tx_0.on()
  elif btnB.wasPressed():
    laser_tx_0.off()
  wait_ms(2)