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
step 0, training accuracy 0.1
step 100, training accuracy 0.91
step 200, training accuracy 0.94
step 300, training accuracy 0.97
step 400, training accuracy 0.86
step 500, training accuracy 0.96
step 600, training accuracy 0.94
step 700, training accuracy 0.96
step 800, training accuracy 0.96
step 900, training accuracy 0.94
test accuracy 0.9703
