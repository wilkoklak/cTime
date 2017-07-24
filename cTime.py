import time
import decimal

class Timer:
	def __init__(self, log=True, precision=10):
		self._log = log
		self._precision = precision
		self._start_time = time.perf_counter()
	def stop(self):
		self._end_time = time.perf_counter()
		self._delta = self._end_time - self._start_time
		r = decimal.Decimal(self._delta)
		r = r.quantize(decimal.Decimal(10) ** -(self._precision))
		if self._log:
			print(r)
		return r
