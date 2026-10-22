from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import module

import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




stepmotor = module.get(module.STEPMOTORDRIVER)



stepmotor.initDevice(0x27)
stepmotor.setStepPulse(500, 0)
stepmotor.setStepPulse(500, 1)
stepmotor.setStepPulse(500, 2)
stepmotor.setStepDir(0, 1)
stepmotor.setStepDir(1, 1)
stepmotor.enableMotor(1)
print(stepmotor.readStatus(0XFE))
print(stepmotor.readStatus(0XFF))
while True:
  stepmotor.resetMotor(0, 1)
  wait(2)
  stepmotor.resetMotor(1, 1)
  wait(2)
  stepmotor.enableMotor(0)
  wait(2)
  stepmotor.enableMotor(1)
  wait(2)
  stepmotor.resetMotor(0, 0)
  wait(2)
  stepmotor.resetMotor(1, 0)
  wait(2)
  wait_ms(2)