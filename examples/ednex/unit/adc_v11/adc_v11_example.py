from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
adc_v11_0 = unit.get(unit.ADCV11, unit.PORTA)








adc_v11_0.set_gain(0x00)
adc_v11_0.set_sample_rate(0x00)
adc_v11_0.set_mode(0x00)
while True:
  print((str('ADC Value:') + str((adc_v11_0.get_adc_raw_value()))))
  print((str('Voltage:') + str((adc_v11_0.get_voltage()))))
  wait_ms(2)