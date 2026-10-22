from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import network
import wifiCfg
import socket
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('', '')
while not (wifiCfg.wlan_sta.isconnected()):
  print('WIFI Connecting...')
  wait(1)
print((str('Server IP:') + str((wlan.ifconfig()))))

udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.bind(('0.0.0.0', 5000))
while True:
  print(udpsocket.recv(1024))
  wait_ms(2)