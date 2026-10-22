from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import machine


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








PWM0 = machine.PWM(26, freq=10000, duty=50, timer=0)
PWM0.freq(1000)
PWM0.duty(50)