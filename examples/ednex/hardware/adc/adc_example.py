from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import machine


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








adc0 = machine.ADC(36)
adc0.width(machine.ADC.WIDTH_9BIT)
adc0.atten(machine.ADC.ATTN_11DB)
print(adc0.read())