from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from libs.mc_espnow import MCESPNOW
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


flag_cb = None
run = None
cnt_success = None
cnt_send = None
peer_mac = None
slave_ssid = None

now = MCESPNOW()

label0 = MCLabel('label0', x=0, y=44, color=0x000000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=1, y=74, color=0x000000, font=FONT_MONT_14, parent=None)
label2 = MCLabel('label2', x=0, y=106, color=0x000000, font=FONT_MONT_14, parent=None)
label4 = MCLabel('press btna', x=122, y=8, color=0x000000, font=FONT_MONT_14, parent=None)

peer_mac = None



def send_cb(flag):
  global flag_cb,run,cnt_success,cnt_send,peer_mac,slave_ssid
  flag_cb = flag
  if flag_cb:
    cnt_success = cnt_success + 1
    label2.set_text(str((str('Send Data/Send Success:') + str(((str(cnt_send) + str(((str('/') + str(cnt_success))))))))))

  pass



def buttonA_wasPressed():
  global flag_cb, run, cnt_success, cnt_send, peer_mac, slave_ssid
  run = 1
  label2.set_text('RUNNING')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  global flag_cb, run, cnt_success, cnt_send, peer_mac, slave_ssid
  run = 0
  label2.set_text('press btna')
  pass
btnC.wasPressed(buttonC_wasPressed)


now.espnow_init(1, 1)
cnt_success = 0
flag_cb = 0
run = 0
cnt_send = 0
slave_ssid = 'M5_Slave'
while peer_mac == None:
  peer_mac = now.espnow_scan(1, slave_ssid)
label0.set_text(str((str('Slave SSID:') + str(slave_ssid))))
label1.set_text(str((str('Peer MAC:') + str(peer_mac))))
now.espnow_add_peer(peer_mac, 1, 0, False)
now.espnow_send_cb(send_cb)
while True:
  if run:
    cnt_send = cnt_send + 1
    now.espnow_send_data(1, str(cnt_send))
    label2.set_text(str((str('Send Data/Send Success:') + str(((str(cnt_send) + str(((str('/') + str(cnt_success))))))))))
    wait(1)
  wait_ms(2)
