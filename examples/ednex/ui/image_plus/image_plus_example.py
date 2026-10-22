from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from libs.image_plus import *
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






imageplus0 = MCImagePlus(110, 70, url='https://makerandcoder.com/MCLab/ImagePlus/Logo.png', timer=True, interval=3000)


wait(1)
imageplus0.setPosition(0, 0)