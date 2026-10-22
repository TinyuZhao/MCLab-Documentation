from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from machine import CAN
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


frame = None



label0 = MCLabel('label0', x=0, y=91, color=0x000000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=0, y=112, color=0x000000, font=FONT_MONT_14, parent=None)
label2 = MCLabel('label2', x=0, y=130, color=0x000000, font=FONT_MONT_14, parent=None)
label3 = MCLabel('label3', x=0, y=152, color=0x000000, font=FONT_MONT_14, parent=None)



def buttonA_wasPressed():
  global frame
  can.send([0, 1, 2, 3, 4, 5, 6, 7], 0)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global frame
  can.clear_tx_queue()
  can.clear_rx_queue()
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global frame
  can.restart()
  pass
btnC.wasPressed(buttonC_wasPressed)


can = CAN(0, extframe=True, mode=CAN.NORMAL, baudrate=CAN.BAUDRATE_25K, tx_io=17, rx_io=16, auto_restart=False)
while True:
  label0.set_text(str(can.state()))
  if can.any():
    frame = can.recv()
    label1.set_text(str(frame[0]))
    label2.set_text(str(frame[1]))
    label3.set_text(str(frame[3]))
  wait_ms(30)
  wait_ms(2)
