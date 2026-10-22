from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import module

import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




module_4in8out = module.get(module.MODULE_4IN8OUT)



module_4in8out.init_i2c_address(0x45)
while True:
  module_4in8out.write_output_pin(0, 1)
  print((str('ch0 state:') + str((module_4in8out.read_input_pin(0)))))
  wait(1)
  module_4in8out.write_output_pin(0, 0)
  print((str('ch0 state:') + str((module_4in8out.read_input_pin(0)))))
  wait(1)
  wait_ms(2)