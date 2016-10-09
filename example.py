import cTime
import time

# A timer that will return a floating point number
cTime.time('timer1', _round=5)

# A timer that will print results itself to the console
cTime.time('timer2', _print=True)
time.sleep(10)
cTime.timeEnd('timer2')
time.sleep(5)
print('Printed timer1: {}'.format(cTime.timeEnd('timer1')))

# See README.md for more details
