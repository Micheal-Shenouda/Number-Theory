# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
"""Continuants + linear congruence demo.

This file implements:
- `continuants(seq)` producing K_0..K_n for sequence `seq`.
- `egcd(a,b)` iterative extended gcd returning (g,x,y) with ax+by=g.
- `solve_linear_congruence(a,y,m)` solving a*x = y (mod m).

Small demo at the bottom.
"""

def continuants(seq):
    """Return list [K_0, K_1, ..., K_n] for sequence `seq`.

    Definitions:
      K_0 = 1
      K_1 = seq[0]  (if seq non-empty)
      K_n = seq[n-1] * K_{n-1} + K_{n-2}
    """
    if not seq:
        return [1]
    K = [1, seq[0]]
    for i in range(2, len(seq) + 1):
        K.append(seq[i - 1] * K[i - 1] + K[i - 2])
    return K


def egcd(a, b):
    """Iterative extended gcd. Returns (g, x, y) with a*x + b*y = g = gcd(a,b)."""
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while b:
        q = a // b
        a, b = b, a - b * q
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def solve_linear_congruence(a, y, m):
    """Solve a * x = y (mod m).

    Returns (x0, mod) where all solutions are x ≡ x0 (mod mod).
    If no solution, returns None.
    """
    g, x0, _ = egcd(a, m)
    if y % g != 0:
        return None
    mod = m // g
    x0 = (x0 * (y // g)) % mod
    return x0, mod


def euclid_quotients(a, b):
    """Return list of quotients produced by Euclidean algorithm on (a,b)."""
    q = []
    while b:
        q.append(a // b)
        a, b = b, a % b
    return q


if __name__ == "__main__":
    # demo continuants
    seq = [3, 7, 2, 5]
    print("seq:", seq)
    print("continuants:", continuants(seq))

    # demo: quotients from Euclid for sample (a,b)
    a0 = 54321
    b0 = 9876
    q = euclid_quotients(a0, b0)
    print("euclid quotients for", a0, b0, ":", q)
    print("continuants of quotients:", continuants(q))

    # egcd demo
    g, x, yv = egcd(a0, b0)
    print(f"gcd({a0},{b0}) = {g}, coeffs: {x}, {yv}  (check: {a0}*{x} + {b0}*{yv} = {a0*x + b0*yv})")

    # linear congruence demo: solve 14 * x = 30 (mod 100)
    demo = solve_linear_congruence(14, 30, 100)
    if demo is None:
        print("No solution for 14*x = 30 (mod 100)")
    else:
        x0, mod = demo
        print(f"Solutions for 14*x = 30 (mod 100): x ≡ {x0} (mod {mod})")