from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from modbus.slave.rtu import ModbusSlave
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


inc = None
D1 = None
D2 = None
D3 = None
data_buf = None



label0 = MCLabel('label0', x=0, y=92, color=0x000000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=0, y=113, color=0x000000, font=FONT_MONT_14, parent=None)
label2 = MCLabel('label2', x=0, y=134, color=0x000000, font=FONT_MONT_14, parent=None)



def buttonA_wasPressed():
  global inc, D1, D2, D3, data_buf
  inc = inc + 1
  if inc >= 2:
    inc = 0
    modbus_s.update_process(1, 10, 3, [D1, D2, D3])
  pass
btnA.wasPressed(buttonA_wasPressed)


modbus_s = ModbusSlave(2, tx=17, rx=16, baudrate=9600, data_bits=8, stop_bits=1, parity=None, slaveID=1)
modbus_s.function_init(1, 10, 3)
D1 = 0
D2 = 0
D3 = 0
inc = 0
while True:
  data_buf = modbus_s.receive_req_create_pdu()
  if (modbus_s.find_function) == (3):
    modbus_s.create_slave_response(data_buf)
    wait_ms(10)
  if inc:
    D1 = D1 + 187
    D2 = D2 + 231
    D3 = D3 + 159
    if D1 >= 0xFFFF:
      D1 = 0
    if D2 >= 0xFFFF:
      D2 = 0
    if D3 >= 0xFFFF:
      D3 = 0
    label0.set_text(str(D1))
    label1.set_text(str(D2))
    label2.set_text(str(D3))
  wait_ms(2)
