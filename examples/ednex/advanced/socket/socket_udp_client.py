from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import socket


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)









udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.connect(('192.168.51.134', 5000))
while True:
  udpsocket.send('Hello MC')
  wait_ms(2)