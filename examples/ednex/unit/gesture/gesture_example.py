from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
gesture_0 = unit.get(unit.GESTURE, unit.PORTA)








gesture_0.begin()
gesture_0.set_gesture_highrate(True)
while True:
  print(gesture_0.get_gesture())
  print(gesture_0.gesture_description((gesture_0.get_gesture())))
  if gesture_0.GestureUp:
    print('up')
  wait(1)
  wait_ms(2)