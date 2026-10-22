from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from comx.nbiot import NBIoT


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








nb = NBIoT(tx=13, rx=5)
nb.reset()
if nb.coap_connect('120.77.157.90', 5683):
  print(nb.coap_get('/m5stack-get'))
  print(nb.coap_post('/m5stack-post', 'post-test', content_format=0))
  print(nb.coap_put('/m5stack-put', 'post-test', content_format=0))