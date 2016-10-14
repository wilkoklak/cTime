# It's console.time from JS in Python3

import time as timee

class CollisionError(Exception):
	pass

class Timer:
	def __init__(self, name, r, p):
		self.start = timee.time()
		self.name = name
		self.r = r
		self.p = p
	def stop(self):
		tDelta = round((timee.time() - self.start) * 1000, self.r)
		if self.p == True:
			print('{} ended in: {} ms'.format(self.name, tDelta))
		else:
			return tDelta

timers = []
names = []
def time(name, _round=2, _print=False):
	if name not in names:
		t = Timer(name, _round, _print)
		timers.append(t)
		names.append(name)
	else:
		raise CollisionError('Timer name already taken!')

def timeEnd(name):
	for t in timers:
		if t.name == name:
			r = t.stop()
			names.remove(t.name)
			timers.remove(t)
			return r
