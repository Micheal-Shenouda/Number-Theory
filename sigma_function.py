from sympy import factorint

def Sigma(n):
    # Compute the sum of divisors function σ(n) using its prime factorization.
    if n < 1:
        print("n must be a positive integer.")
        exit()
    
    prime_factors = factorint(n)
    result = 1
    
    for p, k in prime_factors.items():
        result *= (p**(k + 1) - 1) // (p - 1)
    
    return result

if __name__ == "__main__":
    try:
        while True:
            n = int(input("Enter a positive integer n: "))
            print(f"σ({n}) =", Sigma(n))
    except KeyboardInterrupt:
        exit()