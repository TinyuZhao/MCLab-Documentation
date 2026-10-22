from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from IoTcloud.Azure import IoT_Central
import json
import time
import imu


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


Screen_brightness = None
rtc_year = None
rtc_ymon = None
rtc_mday = None
rtc_hour = None
rtc_min = None
Speaker_local_path = None

imu0 = imu.IMU()




def Screen_brightness_cb(name, value):
  global Screen_brightness, rtc_year, rtc_ymon, rtc_mday, rtc_hour, rtc_min, Speaker_local_path
  Screen_brightness = value
  screen.set_screen_brightness(Screen_brightness)

  result = 200
  return (value, result)

def azure_direct_RTC_set_rtc(payload, rid):
  global Screen_brightness, rtc_year, rtc_ymon, rtc_mday, rtc_hour, rtc_min, Speaker_local_path
  rtc_date, rtc_time = payload[1:-1].split('T')
  rtc_year, rtc_ymon, rtc_mday = rtc_date.split('-')
  rtc_hour, rtc_min, _ = rtc_time.split(':')
  rtc.datetime((int(rtc_year[2:]), int(rtc_ymon), int(rtc_mday), 0, int(rtc_hour), int(rtc_min), 0, 0))

  azurepnp.response_direct_method(0, rid, body='')

def azure_direct_Speaker_play_local(payload, rid):
  global Screen_brightness, rtc_year, rtc_ymon, rtc_mday, rtc_hour, rtc_min, Speaker_local_path
  Speaker_local_path = payload[1:-1]
  speaker.playWAV(Speaker_local_path)

  azurepnp.response_direct_method(0, rid, body='')


azurepnp = IoT_Central(scope_id='<scope-id>', device_id='<device-id>', device_key='<device-key>', model_id='dtmi:m5stack:core:core2;1')
azurepnp.on_property_update('brightness', Screen_brightness_cb)
azurepnp.subscribe_direct_method('RTC*set_rtc', azure_direct_RTC_set_rtc)
azurepnp.subscribe_direct_method('Speaker*play_local', azure_direct_Speaker_play_local)
azurepnp.start()
while True:
  # Send IMU telemetry to Azure
  azurepnp.publish_D2C_message(json.dumps({'AccelX':imu0.acceleration[0],'AccelY':imu0.acceleration[1],'AccelZ':imu0.acceleration[2],'GyroX':imu0.gyro[0],'GyroY':imu0.gyro[1],'GyroZ':imu0.gyro[2]}), "IMU")
  # Update DeviceInformation property to Azure
  azurepnp.update_twin_reported_properties(json.dumps({'DeviceInformation':{'__t':'c', 'manufacturer':'MC','product_name':'MC','device_sn':'123123','device_mac':'12:12:12:12','fw_version':'1'}}))
  wait(1)
  wait_ms(2)
