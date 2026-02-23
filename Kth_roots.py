import Totient
import Bezout_coeff_1
import Successive_Squaring

# We call phi externaly because if we need to use this script in RSA decoding we will not able to find phi in normal way
def phi(m):
    return Totient.Phi(m)

def solve(k, b, phi, m):
    x, y = Bezout_coeff_1.Bezout_coeff_without_printing(k, phi)
    # x, y is the solution of equation a (k) + phi (y) = gcd(k, phi)

    y = -y      # Negative sign because we want the equation become a (k) {-} phi (y) = gcd(k, phi). Not {+}
    if x < 0:   # Need x to be postive
        x += phi
        y += k

    result = Successive_Squaring.succ_squ(b, m, x)
    return(result, x, y)

if __name__ == "__main__":
    print("This method computes the Kth roots Modulo m")
    print("in the form of x**k ≡ b (mod m)")
    k, b, m = int(input("Enter K: ")), int(input("Enter b: ")), int(input("Enter m: "))

    result, x, y = solve(k, b, phi(m), m)
    print(f"\nφ({m}) =", phi(m))
    print(f"\n{x}k - {y}φ({m}) = {k * x - phi(m) * y}")
    print(f"\nthe solution x = {result}")