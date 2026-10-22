from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import nvs


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








nvs.write(str('key'), 'value')
print(nvs.read_str('key'))