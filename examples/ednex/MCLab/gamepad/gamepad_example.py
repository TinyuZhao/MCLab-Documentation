from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from ubt_controller import UBTBLECentral


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


x = None
y = None
addr_type1 = None
addr1 = None
name1 = None

ubtblecentral = UBTBLECentral()





def ubt_right_pos_update_cb(args):
  global x,y,addr_type1,addr1,name1
  x, y = args
  print((str('x:') + str(((str(x) + str(((str(' y:') + str(y)))))))))

  pass

ubtblecentral.set_event(ubtblecentral.JOYSTICK_RIGHT_POS_UPDATE_EVENT, ubt_right_pos_update_cb)


def ubt_left_pos_update_cb(args):
  global x,y,addr_type1,addr1,name1
  x, y = args
  print((str('x:') + str(((str(x) + str(((str(' y:') + str(y)))))))))

  pass

ubtblecentral.set_event(ubtblecentral.JOYSTICK_LEFT_POS_UPDATE_EVENT, ubt_left_pos_update_cb)


def ubtble_central_connect_cb():
  global x,y,addr_type1,addr1,name1
  print(name1)

  pass


def ubtble_central_scan_cb(addr_type, addr, name):
  global x,y,addr_type1,addr1,name1
  addr_type1 = addr_type
  addr1 = addr
  name1 = name
  print(addr_type1)
  print(addr1)
  print(name1)
  if addr1 == None:
    print('No controller found')
  else:
    ubtblecentral.connect(timeout=2000, callback=ubtble_central_connect_cb)

  pass


ubtblecentral.scan(scantime=2000, callback=ubtble_central_scan_cb)


def ubt_button_l1_press_cb(args):
  global x,y,addr_type1,addr1,name1
  print('L1 Press')

  pass

ubtblecentral.set_event(ubtblecentral.BUTTON_L1_PRESS_EVENT, ubt_button_l1_press_cb)


def ubt_button_l2_press_cb(args):
  global x,y,addr_type1,addr1,name1
  print('L2 Press')

  pass

ubtblecentral.set_event(ubtblecentral.BUTTON_L2_PRESS_EVENT, ubt_button_l2_press_cb)


def ubt_button_r1_press_cb(args):
  global x,y,addr_type1,addr1,name1
  print('R1 Press')

  pass

ubtblecentral.set_event(ubtblecentral.BUTTON_R1_PRESS_EVENT, ubt_button_r1_press_cb)


def ubt_button_r2_press_cb(args):
  global x,y,addr_type1,addr1,name1
  print('R2 Press')

  pass

ubtblecentral.set_event(ubtblecentral.BUTTON_R2_PRESS_EVENT, ubt_button_r2_press_cb)
