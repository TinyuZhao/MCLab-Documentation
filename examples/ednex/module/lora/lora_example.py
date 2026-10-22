from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import module



screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


packet_size = None
check = None

lora433 = module.get(module.LORA433)




def lora433_callback(size):
  global packet_size, check, gps, nb
  packet_size = size
  if packet_size:
    check = lora433.read_packet()
    print(check)
  pass

def buttonA_wasPressed():
  global packet_size, check, gps, nb
  lora433.set_begin_packet()
  lora433.write_packet([0x48, 0x65, 0x6C, 0x6C, 0x6F])
  lora433.set_end_packet()
  pass
btnA.wasPressed(buttonA_wasPressed)


lora433.init_lora_module(cs=33, rst=26, irq=36)
lora433.set_lora_config(freq=433000000, band=125000, TxPow=17, sync=0x34, spreadfactor=7, crate=5, preamble=8, CRC=False)
lora433.set_receive_callback_handler(lora433_callback)
