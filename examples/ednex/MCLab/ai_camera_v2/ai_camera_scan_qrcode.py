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
data = None
sub_data = None
x = None
y = None
width = None
height = None

camera = AiCamera(i2c_bus.PORTA)

label1 = MCLabel('label1', x=0, y=86, color=0x000000, font=FONT_MONT_18, parent=None)
label0 = MCLabel('label0', x=2, y=38, color=0x000000, font=FONT_MONT_18, parent=None)




camera.init(0x24, 1000)
while True:
  temp_data = camera.get_qrcode(True)
  if temp_data != None:
    data = temp_data[0]
    sub_data = temp_data[1]
    x = sub_data[0]
    y = sub_data[1]
    width = sub_data[2]
    height = sub_data[3]
    label0.set_text(str((str('data:') + str(data))))
    label1.set_text(str((str('x:') + str(((str(x) + str(((str(',y:') + str(((str(y) + str(((str(',width:') + str(((str(width) + str(((str(',height:') + str(height))))))))))))))))))))))
  else:
    label0.set_text('Not Found QRCode')
    label1.set_text('Not Found QRCode')
  wait(1)
  wait_ms(2)
