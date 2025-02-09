while True: # Loop forever
    quit = input("Do you want to quit? ")
    if quit == "y":
        break

    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        break

    attack = input("Does your elf attempt to steal the gold? ")
    if attack == "y":
        print("Bad choice, you died.")
        break
