from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import i2c_bus


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x00, freq=400000)
i2c0.addr=(0x5C)
print(i2c0.available())