from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_camera import AiCamera
import i2c_bus
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


temp_data = None
id2 = None
x = None
y = None
width = None
height = None

camera = AiCamera(i2c_bus.PORTA)

label0 = MCLabel('label0', x=2, y=38, color=0x000000, font=FONT_MONT_18, parent=None)
touch_button0 = MCBtn(text='Start face learning', x=85, y=160, w=150, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=0, y=80, color=0x000000, font=FONT_MONT_18, parent=None)



def touch_button0_pressed():
  global temp_data, id2, x, y, width, height
  camera.start_face_learning()
  pass
touch_button0.pressed(touch_button0_pressed)


camera.init(0x24, 1000)
while True:
  if (camera.get_recognized_face_count()) > 0:
    temp_data = camera.get_recognized_face(0)
    id2 = temp_data[0]
    x = temp_data[1]
    y = temp_data[2]
    width = temp_data[3]
    height = temp_data[4]
    label0.set_text(str((str('id:') + str(id2))))
    label1.set_text(str((str('x:') + str(((str(x) + str(((str(',y:') + str(((str(y) + str(((str(',width:') + str(((str(width) + str(((str(',height:') + str(height))))))))))))))))))))))
  else:
    label0.set_text('Not Found Face')
    label1.set_text('Not Found Face')
  wait(1)
  wait_ms(2)
