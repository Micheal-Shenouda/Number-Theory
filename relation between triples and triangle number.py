from math import sqrt

for i in range(1, 11):
    n = (i**2 + i) * 2
    if sqrt((n+1)**2 - n**2).is_integer():
        print(F"{i}: triangle={n//4} b={n} ({int(sqrt((n+1)**2 - n**2))},{n},{n+1})   {n//4}")