from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
rfid_0 = unit.get(unit.RFID, unit.PORTA)








while True:
  print(rfid_0.isCardOn())
  print(rfid_0.readUid())
  wait(0.5)
  wait_ms(2)