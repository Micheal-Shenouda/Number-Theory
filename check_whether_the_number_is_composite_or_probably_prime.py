import Successive_Squaring
import random


print('This script shows whether the number is "Composite" or "Probably Prime"')
m = int(input("Enter the number: "))
k = m - 1
a_list = [random.randint(1, k) for i in range(100)]

for a in a_list:
    result = Successive_Squaring.succ_squ(a, m, k)
    if result != 1:
        print(f"The number {m} is composite as {a}**{k} ≅ {result} (mod {m})")
        exit()

print("The number may be prime")
