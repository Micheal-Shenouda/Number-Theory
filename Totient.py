from sympy import factorint

def Phi(n):
    # Compute Euler's Totient function φ(n) using its prime factorization.
    if n < 1:
        print("n must be a positive integer.")
        exit()
    
    prime_factors = factorint(n)
    result = n
    
    for p in prime_factors:
        result *= (1 - 1/p) # φ(n) = n * Π(1 - 1/p)
    
    return int(result)


if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))
    print(f"φ({n}) = φ({factorint(n)}) = {Phi(n)}")