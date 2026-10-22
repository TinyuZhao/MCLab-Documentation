from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






image0 = MCImg("res/default.png", x=110, y=70, parent=None)
image0.x_pos=110
image0.y_pos=70


image0.set_img_src("res/default.png")
wait(1)
image0.set_pos(0, 0)