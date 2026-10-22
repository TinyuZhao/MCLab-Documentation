import bt

# Proof-of-concept of a REPL over BLE UART.
#
# Tested with the Adafruit Bluefruit app on Android.
# Set the EoL characters to \r\n.

import io
import os
import micropython
import machine


_MP_STREAM_POLL = const(3)
_MP_STREAM_POLL_RD = const(0x0001)

# TODO: Remove this when STM32 gets machine.Timer.
if hasattr(machine, "Timer"):
    _timer = machine.Timer(-1)
else:
    _timer = None

# Batch writes into 50ms intervals.
def schedule_in(handler, delay_ms):
    def _wrap(_arg):
        handler()

    if _timer:
        _timer.init(mode=machine.Timer.ONE_SHOT, period=delay_ms, callback=_wrap)
    else:
        micropython.schedule(_wrap, None)


# Simple buffering stream to support the dupterm requirements.
class BLEUARTStream(io.IOBase):
    def __init__(self, uart):
        self._uart = uart
        self._tx_buf = bytearray()
        self._timer = machine.Timer(-2)
        # self._uart.irq(self._on_rx)
        self._timer.init(mode=machine.Timer.PERIODIC, period=200, callback=self._on_rx)

    def _on_rx(self, tim):
        # Needed for ESP32.
        if hasattr(os, "dupterm_notify"):
            os.dupterm_notify(None)

    def read(self, sz=None):
        return self._uart.read(sz)

    def readinto(self, buf):
        avail = self._uart.read(len(buf))
        if not avail:
            return None
        for i in range(len(avail)):
            buf[i] = avail[i]
        return len(avail)

    def ioctl(self, op, arg):
        if op == _MP_STREAM_POLL:
            if self._uart.any():
                return _MP_STREAM_POLL_RD
        return 0

    def _flush(self):
        data = self._tx_buf[0:100]
        self._tx_buf = self._tx_buf[100:]
        self._uart.write(data)
        if self._tx_buf:
            schedule_in(self._flush, 50)

    def write(self, buf):
        empty = not self._tx_buf
        self._tx_buf += buf
        if empty:
            schedule_in(self._flush, 50)



uart = bt.UARTServer()
uart.init()
stream = BLEUARTStream(uart)

os.dupterm(stream)



from m5stack import *
from m5stack_ui import *
from uiflow import *


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)



label0 = M5Label(uart.get_gap_name(), x=88, y=95, color=0x000, font=FONT_MONT_14, parent=None)
label1 = M5Label("CONNECTED" if uart.isconnected() else "DISCONNECTED", x=88, y=135, color=0x000, font=FONT_MONT_14, parent=None)


label0.set_align(ALIGN_CENTER, x=0, y=0, ref=screen.obj)
label1.set_align(ALIGN_CENTER, x=0, y=40, ref=screen.obj)
import time
while uart.isconnected() == False:
    time.sleep(0.01)
label1.set_text('CONNECTED')
