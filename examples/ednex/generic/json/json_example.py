from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from libs.json_py import *
import json



screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


json_object = None







json_object = py_2_json({'author':'mc','people':'100','device':'mcdevice','number':'5'})
print(json.dumps(json_object))
print(get_json_keys(json_object))
print(get_json_key(json_object, 'author'))
print(get_json_values(json_object))
print(get_json_keys_len(json_object))
