def Bezout(w, v, x, g):
    if w == 0:
        y = (g - a * x) // b
        return g, x, y
    t = g % w 
    q = g // w
    s = x - q * v
    x, g = v, w
    v, w = s, t
    return Bezout(w, v, x, g)


if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    g = a
    v = 0
    w = b
    x = 1
    g, x, y = Bezout(w, v, x, g)

    print(f"gcd({a}, {b}) = {g}")
    print(f"If you want to compute ax + by = {g} press {{+}} \nElse if you want to compute ax - by = {g} press {{-}}")
    sign = input()
    print(f"Solution of {a} x {sign} {b} y = {g} is:")
    print(f"x = {x}, y = {eval(f'{sign}{y}')}")  