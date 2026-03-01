#Варіант 13, тому друга формула
import math
m = float(2)
t = 1.2
b = 0.7
c = float(-1)
f = pow(m * math.tan(t) + abs(math.sin(t)), 1/3)
z = m*math.cos(b*t*math.sin(t))+c
results_and_consts = [m, t ,b, c, f, z]
for i in results_and_consts:
    print(("%s" % i).ljust(20, '*'))
