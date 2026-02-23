def Bezout_coeff(a, b): # Returns(GCD, x, y) with ax+by = gcd(a,b)
    x0, y0, x1, y1 = 1, 0, 0, 1

    print("Euclidean algorithm:")
    while b:
        q = a // b
        print(f"{a} = {b} * {q} + {a % b}")

        # Bezout coefficients update
        a, b = b, a - b * q
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    
    return a, x0, y0

# The same pervios method but without printing any step, without return GCD also
def Bezout_coeff_without_printing(a, b): # Returns(GCD, x, y) with ax+by = gcd(a,b)
    x0, y0, x1, y1 = 1, 0, 0, 1

    while b:
        q = a // b
        # Bezout coefficients update
        a, b = b, a - b * q
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    
    return x0, y0

if __name__ == "__main__":
    a, b = int(input("Enter a: ")), int(input("Enter b: "))
    g, x0, y0 = Bezout_coeff(a, b)
    print(f"\ngcd({a}, {b}) = {g}\n\nSolution of {a} x + {b} y = {g} is:")

    if g == 1:
        print(f"(x,y)=({x0},{y0})", end="")
        print(f"\tto check:ax + by = {a *(x0) + b * (y0)}")

    if g > 1:
        i = 0
        while i < g:
            print(f"{i+1}:(x,y)=({x0 + i * b // g},{y0 - i * a // g})", end="")
            print(f"\tto check:ax + by = {a *(x0 + i * b // g) + b * (y0 - i * a // g)}")
            i += 1

    if g == 0:
        print("Any (x,y) belong to Z")

