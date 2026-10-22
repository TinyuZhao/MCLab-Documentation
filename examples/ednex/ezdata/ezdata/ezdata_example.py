from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from flow import ezdata
import wifiCfg


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


i = None

wifiCfg.autoConnect(lcdShow=False)



while True:
  ezdata.setData('eg8T2v0jOZ6M6V7sLPHCkIAwJLdfxTyB', 'my_topic', 'Hello EzData')
  print(ezdata.getData('eg8T2v0jOZ6M6V7sLPHCkIAwJLdfxTyB', 'my_topic'))
  print(ezdata.getCurrentISODateTime())
  ezdata.removeData('eg8T2v0jOZ6M6V7sLPHCkIAwJLdfxTyB', 'my_topic')
  wait_ms(2)