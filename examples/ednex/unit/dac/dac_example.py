from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
dac_0 = unit.get(unit.DAC, unit.PORTA)


i = None







while True:
  for i in range(4):
    dac_0.setVoltage(i,save=True)
    print((str(str(i)) + str('V')))
    wait(1)
  wait_ms(2)
