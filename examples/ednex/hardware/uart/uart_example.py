from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








uart1 = machine.UART(1, tx=17, rx=16)
uart1.init(9600, bits=8, parity=None, stop=1)
uart1.write('abc')
while True:
  print(uart1.read())
  wait_ms(2)