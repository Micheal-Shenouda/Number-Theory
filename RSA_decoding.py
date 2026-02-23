import Kth_roots

print("This script decrypt messages using RSA")

# Initialization
p = int(input("Enter p: "))
q = int(input("Enter q: "))
m = p * q
k = int(input("Enter k: "))

# Asking for input all codes of message
print("Now enter the codes of message.")
print("Press Enter after evey individual code.")
print("If you finished just press Enter twice after the last code.")
print("Codes:")
encrypted_message = []
s = input()
encrypted_message.append(s)
while s:
    s = input()
    encrypted_message.append(s)
encrypted_message.pop()

# Decrypting using RSA
decrypted_message = ""
for b in encrypted_message:
    result, x, y = Kth_roots.solve(k, int(b), (p - 1)*(q - 1) , m)
    decrypted_message += str(result)

# Converting numbers into charachters
for i in range(0, len(decrypted_message), 2):
    if decrypted_message[i:i+2] == "37": # Space " "
        print(" ", end="")
    else:
        print(chr(int(decrypted_message[i:i+2]) + 86), end="")
print()