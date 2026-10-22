from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from emoji import Emoji


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




emoji0 = Emoji(7, 7, 15, 9)



emoji0.show_map([[0,0,0,0,0,0,0],[0,1,0,0,0,1,0],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[0,1,0,0,0,1,0],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0]], 0xff0000)