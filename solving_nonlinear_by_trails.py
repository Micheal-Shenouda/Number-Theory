print("Solving nonlinear congruence equations\nFunction takes the form of:\na0 * x**(n-1) + a1 * x**(n-2) + ... + an")
f = input("Enter the function: ")
m = int(input("Enter the modulus: "))
for x in range(m):
    if eval(f) % m == 0:
        print(f"x = {x}")