from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)








motion = V_0.init(V_0.MOTION)
motion.setMotionDetectThreshold(0)
motion.setDetectMode(0)
while True:
  if (motion.getMaxDiff()) >= 50:
    print('Moved')
  else:
    print('Not Move')
  wait_ms(2)