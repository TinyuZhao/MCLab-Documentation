from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


x = None
i = None





def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)



x = bytearray(5)
x.append(1)
x.append(2)
while True:
  print((str('list length:') + str(len(x))))
  i_end = float(len(x))
  for i in (1 <= i_end) and upRange(1, i_end, 1) or downRange(1, i_end, 1):
    print(x[int(i - 1)])
  wait_ms(2)
