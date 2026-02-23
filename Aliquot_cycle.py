import sigma_function

def main():
    # Initialization of variables
    order = int(input("Enter the order of Aliquot cycle: "))
    c = 1 # Counter
    n = 1 # Pararmeter of sigma function
    head = n # To keep track of the starting point of the cycle, so that we can start from the next number when we find a dead end.
    Aliquot_cycle = []

    while True:
        try:
            s = sigma_function.Sigma(n) - n

            '''
            s =
                n is is self loop
                1 is useless
            s < n and c = 1 means we are going backward from the beaginning
            length cycle > order is useless(we are looking for a cycle of order n)
            '''
            if s == 1 or s == n or (s < n and c == 1) or len(Aliquot_cycle) > order:
                # Dead end, start from the next number
                n, c, Aliquot_cycle, head = new_start(n, c, Aliquot_cycle, head)
                continue

            if Aliquot_cycle != []:
                if Aliquot_cycle[0] == sigma_function.Sigma(Aliquot_cycle[-1]) - Aliquot_cycle[-1]:
                    if len(Aliquot_cycle) == order:
                        with open("Aliquot_cycle.txt", "a") as f:
                            f.write(f"Aliquot_cycle:{c-1} {Aliquot_cycle}\n")
                        # Aliquot cycle found
                        # Let's start new cycle
                        try:
                            order = int(input("Enter the order of Aliquot cycle: "))
                        except KeyboardInterrupt:
                            exit()
                        n = 2
                        c = 1
                        Aliquot_cycle = []
                        head = n
                        continue
                    
            c += 1
            if not n in Aliquot_cycle:
                # To prevent repeation
                Aliquot_cycle.append(n)
            else:
                n, c, Aliquot_cycle, head = new_start(n, c, Aliquot_cycle, head)
                continue
            n = s
            print(order)

        except KeyboardInterrupt:
            try:
                order = int(input("Enter the order of Aliquot cycle: "))
            except KeyboardInterrupt:
                exit()


def new_start(n, c, Aliquot_cycle, head):
    n = head + 1
    c = 1
    Aliquot_cycle = []
    head = n
    return n, c, Aliquot_cycle, head

main()