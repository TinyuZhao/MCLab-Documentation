from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
remoteInit()

screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


switch_value = None
slider_value = None
input_value = None
stepper_value = None
joystick_x_value = None
joystick_y_value = None
rp_label1_data = None
rp_img1_url = None
rp_gauge1_data = None








def button_1_callback():
  global rp_label1_data, rp_img1_url, rp_gauge1_data, switch_value, slider_value, input_value, stepper_value, joystick_y_value, joystick_x_value 
  pass
def switch_1_callback(switch_value):
  global rp_label1_data, rp_img1_url, rp_gauge1_data, slider_value, input_value, stepper_value, joystick_y_value, joystick_x_value 
  print(switch_value)

def slider_1_callback(slider_value):
  global rp_label1_data, rp_img1_url, rp_gauge1_data, switch_value, input_value, stepper_value, joystick_y_value, joystick_x_value 
  print(slider_value)

def label_1_callback():
  global rp_label1_data, rp_img1_url, rp_gauge1_data, switch_value, slider_value, input_value, stepper_value, joystick_y_value, joystick_x_value 
  return str(rp_label1_data)
def input_1_callback(input_value):
  global rp_label1_data, rp_img1_url, rp_gauge1_data, switch_value, slider_value, stepper_value, joystick_y_value, joystick_x_value 
  print(input_value)

def image_1_callback():
  global rp_label1_data, rp_img1_url, rp_gauge1_data, switch_value, slider_value, input_value, stepper_value, joystick_y_value, joystick_x_value 
  return rp_img1_url
def stepper_1_callback(stepper_value):
  global rp_label1_data, rp_img1_url, rp_gauge1_data, switch_value, slider_value, input_value, joystick_y_value, joystick_x_value 
  print(stepper_value)


def joystick_1_callback(joystick_x_value, joystick_y_value):
  global rp_label1_data, rp_img1_url, rp_gauge1_data, switch_value, slider_value, input_value, stepper_value 
  print(joystick_y_value)
  print(joystick_x_value)

def gauge_1_callback():
  global rp_label1_data, rp_img1_url, rp_gauge1_data, switch_value, slider_value, input_value, stepper_value, joystick_y_value, joystick_x_value 
  return str(rp_gauge1_data)
lcd.qrcode('http://mclab.ai/remote?id=undefined', 72, 32, 176)
