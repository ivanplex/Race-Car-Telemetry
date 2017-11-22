import math

shift = 10 * math.sin(i/41)

for i in range(256):
	val = (i-50)*(i-100)*(i-200)*(i-238) / -60000
	if val > 255:
		val = 255
	elif val < 0:
		val = 0
	#print val
	return val