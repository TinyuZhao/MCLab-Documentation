from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import machine


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








pin0 = machine.Pin(0, mode=machine.Pin.IN, pull=machine.Pin.PULL_UP)
while True:
  pin0.on()
  wait_ms(2)