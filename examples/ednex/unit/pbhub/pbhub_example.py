from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import i2c_bus
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
pahub_0 = unit.get(unit.PAHUB, unit.PORTA, 0x70)
tof_1 = unit.get(unit.TOF, unit.PAHUB0)






label0 = MCLabel('label0', x=119, y=101, color=0x000000, font=FONT_MONT_14, parent=None)


i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x00, freq=400000)
pahub_0.select(0, 0)
print('Close')
pahub_0.select(0, 1)
while True:
  label0.set_text(str(tof_1.distance))
  print(tof_1.distance)
  wait_ms(2)