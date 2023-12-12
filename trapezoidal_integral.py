
from math import sin
from math import pi
from math import sqrt
from math import exp
# --example--
# print(sin(0))
# >>> 0
# -----------


def func1(m):
    return sin(m)


def func2(m):
    return 4/(1+m**2)


def func3(m):
    return sqrt(pi)*exp(-m**2)


def area(f, a=0, b=1, N=100):
    h = (b-a)/N
    menseki = 0.0
    for i in range(N):
        menseki += ((h/2))*(f((a+i*h))+f(a + (i+1)*h))

    return float(menseki)


# (1)
print(area(func1, 0, pi/2, 50))

# (2)
print(area(func2, 0, 1, 100))

# (3)
print(area(func3, -100, 100, 1000))
