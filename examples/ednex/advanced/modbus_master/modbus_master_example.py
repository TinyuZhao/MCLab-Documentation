from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from modbus.master.uModBusSerial import uModBusSerial


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






label0 = MCLabel('label0', x=1, y=113, color=0x000000, font=FONT_MONT_14, parent=None)

def buttonA_wasPressed():
  # global params
  label0.set_text(str(modbus.read_holding_registers(4, 10, 3, False, timeout=2000)))
  pass
btnA.wasPressed(buttonA_wasPressed)


modbus = uModBusSerial(2, tx=17, rx=16, baudrate=9600, data_bits=8, stop_bits=1, parity=None, ctrl_pin=None)