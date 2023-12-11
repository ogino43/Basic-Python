
from math import sin
from math import pi
# --example--
# print(sin(0))
# >>> 0
# -----------

a = 0.0
b = pi/2
N = 100.0
h = (b-a)/N
area = 0.0

for i in range(100):
    area += ((h/2))*(sin((a+i*h))+sin(a + (i+1)*h))

print(area)
