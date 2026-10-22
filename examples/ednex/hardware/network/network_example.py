from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import wifiCfg


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








wifiCfg.doConnect('your-ssid', 'your-password')