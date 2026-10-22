from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
finger_0 = unit.get(unit.FINGER, unit.PORTC)






touch_button0 = MCBtn(text='add user', x=27, y=132, w=100, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button1 = MCBtn(text='remove user', x=190, y=132, w=100, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
label0 = MCLabel('label0', x=129, y=69, color=0x000000, font=FONT_MONT_14, parent=None)

def finger_0_cb(user_id, access):
  # global params
  if (access) == 1 and (user_id) == 1:
    rgb.setColorAll(0x33ff33)
    wait(1)
    rgb.setColorAll(0x000000)
  pass
finger_0.readFingerCb(callback=finger_0_cb)

def buttonA_wasPressed():
  # global params
  finger_0.removeAllUser()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  finger_0.addUser(1, 1)
  pass
btnB.wasPressed(buttonB_wasPressed)


while True:
  label0.set_text(str(finger_0.state))
  wait_ms(2)