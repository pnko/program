"""
from time import sleep, time

sleep(3)
start = time()
print('Quick, hit the Enter key')
input()
reaction_time = time() - start
print('You t'
      'ook', reaction_time, 'seconds')
"""


"""
from gpiozero import LED
red_led = LED(17)
while True:
  red_led.on()
  sleep(1)
  red_led.off()
  sleep(1)

"""

"""
from gpiozero import LED
from time import sleep
red_led.blink(0.2, 0.1, 5)

red_led.toggle()
sleep(1)
print(red_led.is_lit)
red_led.toggle()
sleep(1)
print(red_led.is_lit)

"""

