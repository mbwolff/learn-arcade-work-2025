def main():
    print("Here are instructions for the game.")

    thirst = 0
    miles_traveled = 0
    camel_tiredness = 0
    miles_natives_traveled = -20
    drinks_in_canteen = 3

    done = False

    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ")

        if user_choice.upper() == "Q":
            done = True
            print("OK, game over.")
        elif user_choice.upper() == "E":
            print("My status")

main()