from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
servo_0 = unit.get(unit.SERVO, unit.PORTC)








servo_0.write_angle(0)
servo_0.write_angle(600)