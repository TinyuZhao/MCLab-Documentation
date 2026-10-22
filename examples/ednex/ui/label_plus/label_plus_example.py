from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from libs.label_plus import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






labelplus0 = MCLabelPlus('labelplus0', x=74, y=76, color=0x000000, font=FONT_MONT_14, parent=None, url='https://makerandcoder.com/MCLab/LablePlus/Hello.html', json=None, timer=True, interval=1000, error_msg='Error', error_color=0xff0000)


labelplus0.set_text('Hello MC4.0')
labelplus0.set_text_color(0xff0000)
labelplus0.set_text_font(FONT_MONT_22)
print(labelplus0.get_width())