import time
start = time.perf_counter() # Just to know the runtime

print("This script calculates a^k (mod m) using successive squaring method")
a, m, k = int(input("Enter a: ")), int(input("Enter m: ")), int(input("Enter k: "))

result = 1


while k >= 1:
    if k % 2 == 1:
        result = a * result % m
        k -= 1
    a = a**2 % m
    k //= 2 

print(f"result: {result}")

end = time.perf_counter()
print(f"Runtime: {end - start:} seconds")
