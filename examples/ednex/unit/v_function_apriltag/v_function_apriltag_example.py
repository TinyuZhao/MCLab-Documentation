from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)








tag = V_0.init(V_0.APRILTAG)
while True:
  print((str('AprilTag location: ') + str((tag.getAprilTagcodeLocation()))))
  print((str('AprilTag rotation: ') + str((tag.getAprilTagcodeRotation()))))
  print((str('AprilTag translation: ') + str((tag.getAprilTagcodeTranslation()))))
  wait_ms(2)