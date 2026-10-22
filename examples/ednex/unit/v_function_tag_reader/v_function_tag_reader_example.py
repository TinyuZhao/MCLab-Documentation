from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)








tag_reader = V_0.init(V_0.TAG_READER)
while True:
  print((str('Total number: ') + str((tag_reader.getTotalNumber()))))
  print((str('Tag location: ') + str((tag_reader.getTagLocation(number=0)))))
  print((str('Code: ') + str((tag_reader.getCode(number=0)))))
  print((str('Binstr: ') + str((tag_reader.getBinstr(number=0)))))
  wait_ms(2)