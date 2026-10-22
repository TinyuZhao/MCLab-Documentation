from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)








qr = V_0.init(V_0.QR_CODE)
while True:
  print((str('QRcode version: ') + str((qr.getQRversion()))))
  print((str('Code text: ') + str((qr.getQRtext()))))
  wait_ms(2)