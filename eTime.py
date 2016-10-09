# It's console.time from JS in Python3

import time
from decimal import Decimal

class CollisionError(Exception):
	pass

class Timer:
	def __init__(self, name, r, t):
		self.start = time.time()
		self.name = name
		self.r = r
		self.type = t
	def stop(self):
		tDelta = round((time.time() - self.start) * 1000, self.r)
		if(self.type == 'print'):
			print('{} ended in: {} ms'.format(self.name, tDelta))
		else:
			return tDelta

timers = []
names = []
def timeStart(name, r=2, t='print'):
	if name not in names:
		t = Timer(name, r, t)
		timers.append(t)
		names.append(name)
	else:
		raise CollisionError('Timer name already taken!')

def timeStop(name):
	for t in timers:
		if t.name == name:
			r = t.stop()
			names.remove(t.name)
			timers.remove(t)
			return r
