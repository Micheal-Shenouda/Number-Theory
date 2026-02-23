import math
triangle = []
square = []
for i in range(1,20000000):
    triangle.append(int(i*(i+1)/2))
    square.append(i**2)

i = 0

try:
    for sq in square:
        while triangle[i] <= sq:
            if sq == triangle[i]:
                print(int(math.sqrt(sq)))
                break
            i += 1
except IndexError:
    exit()
