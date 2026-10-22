from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from IoTcloud.Azure import IoT_Hub
from MCLab.gyro_imu import Gyro
import json

import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


twinmsg = None
methodmsg = None
c2dmsg = None
status = None
gyro_x = None
gyro_y = None
gyro_z = None
data = None

gyro = Gyro()

label0 = MCLabel('label0', x=1, y=29, color=0x000000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=0, y=58, color=0x000000, font=FONT_MONT_14, parent=None)
label2 = MCLabel('label2', x=0, y=83, color=0x000000, font=FONT_MONT_14, parent=None)
label3 = MCLabel('label3', x=0, y=106, color=0x000000, font=FONT_MONT_14, parent=None)
label4 = MCLabel('label4', x=0, y=139, color=0x000000, font=FONT_MONT_14, parent=None)




def azure_desired_cb(payload):
  global twinmsg, methodmsg, c2dmsg, status, gyro_x, gyro_y, gyro_z, data
  twinmsg = payload
  label0.set_text(str(twinmsg))




def azure_direct_rgb(payload, rid):
  global twinmsg, methodmsg, c2dmsg, status, gyro_x, gyro_y, gyro_z, data
  methodmsg = payload
  label0.set_text(str(methodmsg))
  if '"ON"' == methodmsg:
    label4.set_text('ON')
    rgb.setColorAll(0xffff00)
    azure.update_twin_reported_properties(rgb='ON')
    status = 204
  elif '"OFF"' == methodmsg:
    label4.set_text('OFF')
    rgb.setColorAll(0x000000)
    azure.update_twin_reported_properties(rgb='OFF')
    status = 204
  else:
    status = 400

  azure.response_direct_method(0, rid, body='success')


def azure_C2D_cb(msg_data):
  global twinmsg, methodmsg, c2dmsg, status, gyro_x, gyro_y, gyro_z, data
  c2dmsg = msg_data
  label0.set_text(str(c2dmsg))
  pass


azure = IoT_Hub(connection_string='HostName=<hub>.azure-devices.net;DeviceId=<device-id>;SharedAccessKey=<device-key>')
azure.subscribe_C2D_message(azure_C2D_cb)
azure.subscribe_twin_desired_response(azure_desired_cb)
azure.subscribe_direct_method('rgb', azure_direct_rgb)
azure.start()
label0.set_text(str(azure.retrieve_twin_properties()))
gyro.init()
while True:
  gyro_x = gyro.get_gyro(0)[0]
  gyro_y = gyro.get_gyro(0)[1]
  gyro_z = gyro.get_gyro(0)[2]
  label1.set_text(str(gyro_x))
  label2.set_text(str(gyro_y))
  label3.set_text(str(gyro_z))
  data = {'gyro_x':gyro_x,'gyro_y':gyro_y,'gyro_z':gyro_z}
  azure.publish_D2C_message(str((json.dumps(data))))
  wait(5)
  wait_ms(2)
