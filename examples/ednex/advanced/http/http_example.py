from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import urequests


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








try:
  req = urequests.request(method='GET', url='https://httpbin.org/get', headers={'Accept':'application/json'})
  print((str('Status:') + str((req.status_code))))
  print(req.text)
  gc.collect()
  req.close()
except:
  print((str('Status:') + str((req.status_code))))
  print('Fail')