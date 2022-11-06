﻿import math
a = float(input("please, enter a:"))
b = float(input("please, enter b:"))
c = float(input("please, enter c:"))

if a == 0:
    print("a can not be 0")
else:
    discriminant = (b*b)-4*a*c

if discriminant < 0:
    print("There are no real roots")
if discriminant == 0:
    x = (-b/(2*a))
    print("x = " + x)
if discriminant > 0:
    fx = ((-b+(math.sqrt(discriminant)))/(2*a))
    sx = ((-b-(math.sqrt(discriminant)))/(2*a))
    print("There are two roots: " + fx + "and " + sx)
