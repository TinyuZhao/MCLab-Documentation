from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from libs.mc_espnow import MCESPNOW


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


mac_addr = None
data = None
one_time = None
ssid = None

now = MCESPNOW()

label0 = MCLabel('label0', x=0, y=49, color=0x000000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=0, y=71, color=0x000000, font=FONT_MONT_14, parent=None)
label2 = MCLabel('label2', x=0, y=91, color=0x000000, font=FONT_MONT_14, parent=None)




def recv_cb(dummy):
  global mac_addr,data,one_time,ssid
  mac_addr, data = now.espnow_recv_str()
  label1.set_text(str((str('Slave MAC:') + str(mac_addr))))
  label2.set_text(str((str('Receive data:') + str(data))))
  if one_time:
    now.espnow_add_peer(mac_addr, 1, 0, False)
    now.espnow_recv_cb(recv_cb)
    one_time = 0

  pass




now.espnow_init(1, 1)
one_time = 1
ssid = 'M5_Slave'
data = 0
now.espnow_set_ap(ssid, '')
label0.set_text(str((str('SSID:') + str(ssid))))
now.espnow_recv_cb(recv_cb)
