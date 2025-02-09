keep_going = "yes"

while keep_going == "yes":
    a = input("Would you like to try again? ").lower()
    if a == "no":
        keep_going = a
    else:
        print("OK, let's keep going!")
