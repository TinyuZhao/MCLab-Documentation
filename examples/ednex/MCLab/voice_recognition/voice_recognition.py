from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_tools import *
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


recv_voice_cmd = None

voice = VoiceRecognize()

label0 = MCLabel("label0", x=0, y=201, color=0x000000, font=FONT_MONT_14, parent=None)
label2 = MCLabel(
    'Pls Say"Hi MC"', x=0, y=6, color=0x000, font=FONT_MONT_34, parent=None
)


def voice_recognize_cmd_callback(voice_cmd):
    global recv_voice_cmd
    recv_voice_cmd = voice_cmd
    pass


voice.set_voice_recognize_cb(voice_recognize_cmd_callback)


voice.init(uart_id=2, tx_pin=27, rx_pin=19)
while True:
    voice.set_voice_recognize_loop()
    if voice.get_voice_recognize_wakeup_status():
        rgb.setColorAll(0x33FF33)
        wait(0.5)
        rgb.setColorAll(0x000000)
        wait(0.5)
        if voice.get_voice_recognize_command() == 0x46:
            label2.set_text("SAY HI")
        elif voice.get_voice_recognize_command() == 0x47:
            label2.set_text("SMILE")
        elif voice.get_voice_recognize_command() == 0x48:
            label2.set_text("JOKE")
        elif voice.get_voice_recognize_command() == 0x01:
            label2.set_text("Moving Forward")
            screen.set_screen_bg_color(0x33FF33)
        elif voice.get_voice_recognize_command() == 0x02:
            label2.set_text("Moving Backward")
            screen.set_screen_bg_color(0x3366FF)
        elif voice.get_voice_recognize_command() == 0x03:
            label2.set_text("Rotating left")
            screen.set_screen_bg_color(0xCC66CC)
        elif voice.get_voice_recognize_command() == 0x04:
            screen.set_screen_bg_color(0xFFFF00)
            label2.set_text("Rotating Right")
        elif voice.get_voice_recognize_command() == 0x09:
            screen.set_screen_bg_color(0xFF0000)
            label2.set_text("STOP")
        elif voice.get_voice_recognize_command() == 0x99:
            label2.set_text("Hi MC")
        else:
            pass
    label0.set_text(
        str((str("voice cmd: ") + str((voice.get_voice_recognize_command()))))
    )
    wait_ms(20)
    wait_ms(2)
