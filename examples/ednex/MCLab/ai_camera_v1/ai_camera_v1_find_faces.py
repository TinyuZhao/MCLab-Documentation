from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_tools import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


result = None

unitv_base = UnitVBase()
face_detect = FaceDetect(unitv_base)

label0 = MCLabel('label0', x=0, y=113, color=0x000000, font=FONT_MONT_14, parent=None)




face_detect.init()
while True:
  print(face_detect.get_face_number())
  if (face_detect.get_face_number()) > 0:
    result = face_detect.get_face_detials(0)
  else:
    result = 'Not find face'
  label0.set_text(str(result))
  print(result)
  wait_ms(2)
