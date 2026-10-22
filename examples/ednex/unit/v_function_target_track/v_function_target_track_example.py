from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)








target = V_0.init(V_0.TARGET_TRACK)
target.setTrackAreaCoordinate(50, 50, 30, 30)
while True:
  print((str('X :') + str(((str((target.getBoxDetail())[0]) + str(((str('Y :') + str((target.getBoxDetail())[2])))))))))
  wait(1)
  wait_ms(2)