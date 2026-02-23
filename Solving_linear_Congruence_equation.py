import Bezout_coeff_1

def steps(a, m, c):
    print("Solving equation of type: a x = c (mod m)")
    g, x0, y0 = Bezout_coeff_1.Bezout_coeff(a, m)
    if c % g != 0:
        print(f"The equation {a}x={c}(mod {m}) has no solutions")
        exit()
    x0 = x0 * c // g
    if x0 < 0:
        x0 += m
    return g, x0

if __name__ == "__main__":
    a, m, c = int(input("Enter a: ")), int(input("Enter m: ")), int(input("Enter c: "))
    g, x0 = steps(a, m, c)
    print(f"{1}:x={x0}", end="")
    print(f"\tto check:{a}x = {a * x0 % m} (mod {m})")

    if g > 1:
        i = 1
        while i < g:
            print(f"{i+1}:x={(x0 + i * m // g) % m}", end="")
            print(f"\tto check:{a}x = {(a *(x0 + i * m // g)) % m} (mod {m})")
            i += 1

