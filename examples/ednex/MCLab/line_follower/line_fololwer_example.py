from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.robocar import Robocar
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


b1 = None
b2 = None
b3 = None
b4 = None
b5 = None

robo = Robocar()

label0 = MCLabel('label0', x=7, y=69, color=0x000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=66, y=69, color=0x000, font=FONT_MONT_14, parent=None)
label2 = MCLabel('label2', x=138, y=69, color=0x000, font=FONT_MONT_14, parent=None)
label3 = MCLabel('label3', x=200, y=69, color=0x000, font=FONT_MONT_14, parent=None)
label4 = MCLabel('label4', x=262, y=69, color=0x000, font=FONT_MONT_14, parent=None)


# Describe this function...
def Method1():
  global b1, b2, b3, b4, b5, i2c0
  label0.set_text(str(robo.ow_multi_line_get_sensor_value(id=1, data_type=0)))
  label1.set_text(str(robo.ow_multi_line_get_sensor_value(id=2, data_type=0)))
  label2.set_text(str(robo.ow_multi_line_get_sensor_value(id=3, data_type=0)))
  label3.set_text(str(robo.ow_multi_line_get_sensor_value(id=4, data_type=0)))
  label4.set_text(str(robo.ow_multi_line_get_sensor_value(id=5, data_type=0)))

# Describe this function...
def method2():
  global b1, b2, b3, b4, b5, i2c0
  (b1, b2, b3, b4, b5) = robo.ow_multi_line_get_sensor_values()
  label0.set_text(str(b1))
  label1.set_text(str(b2))
  label2.set_text(str(b3))
  label3.set_text(str(b4))
  label4.set_text(str(b5))



robo.ow_line_port_init(unit.PORTB)
while True:
  Method1()
  wait_ms(2)
