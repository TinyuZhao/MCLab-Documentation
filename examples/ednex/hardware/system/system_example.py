from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import machine


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)







def buttonB_wasPressed():
  global wdt, pin0, PWM0, adc0, dac0, uart1, i2c0
  machine.reset()
  pass
btnB.wasPressed(buttonB_wasPressed)

