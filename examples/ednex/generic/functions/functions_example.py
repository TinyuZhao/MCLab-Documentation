from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


x = None




import random


# Describe this function...
def dosomething(x):
  print(x)



while True:
  dosomething(random.randint(0, 255))
  wait(1)
  wait_ms(2)
