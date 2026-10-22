from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.robocar import Robocar
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


value = None

robo = Robocar()

label0 = MCLabel('label0', x=1, y=113, color=0x000000, font=FONT_MONT_14, parent=None)




robo.ultrasonic_port_init(unit.PORTC)
robo.ultrasonic_rgb_color_from(1, 6, 0x33ff33, 100)
while True:
  value = robo.ultrasonic_rgb_sensor(mode=1)
  print(value)
  label0.set_text(str(value))
  wait_ms(2)
