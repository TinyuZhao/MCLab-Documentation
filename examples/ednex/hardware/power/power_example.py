from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.robocar import Robocar


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




robo = Robocar()



screen.set_screen_brightness(30)
power.setPowerLED(True)
print(robo.get_encoder_vin_voltage())