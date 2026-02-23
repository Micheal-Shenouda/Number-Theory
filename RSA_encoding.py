import Successive_Squaring

print("This script encrypt messages using RSA")
m = int(input("Enter m: "))
k = int(input("Enter a number which is realtivly prime to φ(m): ")) # Power
message = input("Enter the message: ")

# Converting characters into numbers quite bit like ascii
# # For example a = 11, b = 12, ...., z = 36
s = ""  
for c in message:
    if c.isalpha():
        s += str(ord(c.lower()) - 86)
    elif c == " ":
        s += "37"

# Now let's divided the numbers in string s into separate numbers
# less than the (digits number) of m
array_of_s = []
l = len(str(m))
for i in range(0, len(s), l-1):
    array_of_s.append(s[i:l+i-1])

# RSA Encoding
for num in array_of_s:
    print(Successive_Squaring.succ_squ(int(num), m, k))
    
