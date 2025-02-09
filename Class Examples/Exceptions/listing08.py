# Generating exceptions
def get_input():
    text_entered = False
    while not text_entered:
        user_input = input("Enter something: ")
        if len(user_input) == 0:
            print("Please try again.")
        else:
            return user_input


get_input()
