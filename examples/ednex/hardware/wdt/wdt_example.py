from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from machine import WDT
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








wdt = WDT(timeout=5000)
while True:
  wait(3000)
  wdt.feed()
  wait_ms(2)