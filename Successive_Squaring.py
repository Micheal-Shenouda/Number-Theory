def succ_squ(a, m, k):

    # Initialization
    b = bin(k)
    binary_list = list(b[2:])  # Remove the '0b' prefix
    power_list = []     # Binary decomposition of k, for example if k = 13 then power_list will be [0, 2, 3] because 13 = 2^0 + 2^2 + 2^3
    a_power_k_mod_m_list = [a % m]

    # Declaring the power_list and a_power_k_mod_m_list
    power_list = [len(binary_list) - i for i in range(len(binary_list), 0, -1) if binary_list[i-1] != '0']
    loop_boundry = max(power_list) # Needed for a_power_k_mod_m_list
    for i in range(loop_boundry):
        a_power_k_mod_m_list.append(a_power_k_mod_m_list[-1] ** 2 % m)

    # Multiplying the necessary powers of a together to get the final result
    result = 1
    for i in power_list:
        result = result * a_power_k_mod_m_list[i] % m
        
    return result
    
if __name__ == "__main__":
    print("This script calculates a^k (mod m) using successive squaring method")
    a, m = int(input("Enter a: ")), int(input("Enter m: "))
    print("For k you can enter a large number\nFor example you can enter 10**1000000")
    k = eval(input("Enter k: "))

    result = succ_squ(a, m, k)
    print(f"result: {result}")

