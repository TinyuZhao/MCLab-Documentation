from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_camera import AiCamera
import i2c_bus


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


is_found = None
location = None
temp_data = None
x = None
y = None
width = None
height = None

camera = AiCamera(i2c_bus.PORTA)

label0 = MCLabel('label0', x=2, y=38, color=0x000000, font=FONT_MONT_18, parent=None)




camera.init(0x24, 1000)
camera.set_tracking_color_id(1)
while True:
  temp_data = camera.get_tracked_color_block()
  is_found = temp_data[0]
  location = temp_data[1]
  x = location[0]
  y = location[1]
  width = location[2]
  height = location[3]
  if is_found:
    label0.set_text(str((str('x:') + str(((str(x) + str(((str(',') + str(((str('y:') + str(((str(y) + str(((str(',') + str(((str('width:') + str(((str(width) + str(((str(',') + str(((str('height') + str(height)))))))))))))))))))))))))))))))
  else:
    label0.set_text('Not Found Red Color')
  wait_ms(2)
