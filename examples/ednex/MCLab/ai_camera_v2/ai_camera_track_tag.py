from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_camera import AiCamera
import i2c_bus


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


temp_data = None
id2 = None
rotation = None
x = None
y = None
width = None
height = None

camera = AiCamera(i2c_bus.PORTA)

label0 = MCLabel('label0', x=2, y=38, color=0x000000, font=FONT_MONT_18, parent=None)




camera.init(0x24, 1000)
while True:
  if (camera.get_tag_count()) > 0:
    temp_data = camera.get_tag(0)
    id2 = temp_data[0]
    rotation = temp_data[1]
    x = temp_data[2]
    y = temp_data[3]
    width = temp_data[4]
    height = temp_data[5]
    label0.set_text(str((str('id:') + str(((str(id2) + str(((str(',rotation:') + str(((str(rotation) + str(((str(',x:') + str(((str(x) + str(((str(',') + str(((str('y:') + str(y)))))))))))))))))))))))))
  else:
    label0.set_text('Not Found Tag')
  wait_ms(2)
