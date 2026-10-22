from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from IoTcloud.AWS import AWS
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








aws = AWS(things_name='UIFlow_TEST', host='xxxxxxxxxxx-ats.iot.ap-southeast-1.amazonaws.com', port=8883, keepalive=60, cert_file_path='', private_key_path='')
aws.start()
while True:
  aws.publish(str('pubtopic'),str('hello'))
  wait(4)
  wait_ms(2)