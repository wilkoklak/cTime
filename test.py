import eTime
import time

eTime.timeStart('x1', 0, 'x')
eTime.timeStart('x2')
for i in range(0, 100000):
	print(i)
print(eTime.timeStop('x1'))
eTime.timeStop('x2')
