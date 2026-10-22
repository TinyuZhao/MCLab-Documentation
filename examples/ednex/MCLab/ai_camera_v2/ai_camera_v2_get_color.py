from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_camera import AiCamera
import i2c_bus


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


color = None
r = None
g = None
b = None

camera = AiCamera(i2c_bus.PORTA)

touch_button0 = MCBtn(text='button0', x=125, y=153, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
label0 = MCLabel('label0', x=2, y=38, color=0x000000, font=FONT_MONT_22, parent=None)



def touch_button0_pressed():
  global color, r, g, b
  color = camera.get_color_rgb()
  r = color[0]
  g = color[1]
  b = color[2]
  label0.set_text(str((str('color:') + str(((str(r) + str(((str(',') + str(((str(g) + str(((str(',') + str(b))))))))))))))))
  pass
touch_button0.pressed(touch_button0_pressed)


camera.init(0x24, 1000)
