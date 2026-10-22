from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






label0 = MCLabel('label0', x=110, y=102, color=0x000000, font=FONT_MONT_14, parent=None)


speaker.playTone(220, 1, volume=6)
wait(1)
speaker.playTone(220, 1, volume=6)
wait(1)