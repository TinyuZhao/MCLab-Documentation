from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
co2_1 = unit.get(unit.CO2_SCD40, unit.PORTA)








co2_1.stop_periodic_measurement()
print(co2_1.serial_number())
print(co2_1.get_calibration_enabled())
co2_1.start_periodic_measurement()
wait(1)
while True:
  if co2_1.data_isready():
    co2_1.read_sensor_measurement()
    print((str('data status:') + str((co2_1.data_isready()))))
    print((str('CO2:') + str((co2_1.co2))))
    print((str('Temperature:') + str((co2_1.temperature))))
  wait_ms(2)