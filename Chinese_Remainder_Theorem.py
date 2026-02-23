from math import prod
from Crypto.Util.number import inverse

i = 1
c = []
m = []

print("Solving system of congruences using\nChinese Remainder Theorem.")
print("Enter equations one by one in the form of x = c mod m.")
print("Press Ctrl+C to stop.")
while True:
    try:
        tmp = input(f"equation {i}: ").split()
        if tmp[0] != 'x' and tmp[0] != 'X' or tmp[1] != '=' or tmp[3] != 'mod' or not tmp[2].isnumeric() or not tmp[4].isnumeric():
            print("Invalid format. Please enter in the form: x = a mod m")
            continue
        c.append(int(tmp[2]))
        m.append(int(tmp[4]))
        i += 1

    except KeyboardInterrupt:
        print("\nInput ended.")
        break


M = 1 * prod(m)
y = [inverse(M // m[i], m[i]) for i in range(len(m))]
x = sum(c[i] * (M // m[i]) * y[i] for i in range(len(m))) % M
print(f"The solution is: {x} mod {M}")