from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from mcmqtt import MCmqtt


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)







def fun__dev_sub_(topic_data):
  global wdt, pin0, PWM0, adc0, dac0, uart1, i2c0
  print('topic: /dev/sub received:')
  print(topic_data)
  pass


mcmqtt = MCmqtt('id_123456', 'broker.emqx.io', 1883, 'user_123456', 'pwd_123456', 300)
mcmqtt.subscribe(str('/dev/sub'), fun__dev_sub_)
print('MQTT Connecting...')
mcmqtt.set_last_will(str('/dev/last_will'),str('device disconnect'))
mcmqtt.start()
print('MQTT Connected')
while True:
  mcmqtt.publish(str('/dev/pub'), str('Hello'), 0)
  wait_ms(2)