from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from hardware import sdcard


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








sdcard.SDCard(20000000)
while True:
  with open('/sd/FileName.*', 'r') as fs:
    lcd.print((fs.read()), 0, 0, 0xffffff, rotate=0)
  wait_ms(2)