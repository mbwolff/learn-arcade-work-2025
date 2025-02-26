user_name = input("What is your name? ")

# This does not work! It will always be true
# if user_name == "Paul" or "Mary":

# This will work
if user_name.lower() == "mark" or user_name.lower() == "mary":
    print("You have a nice name.")
else:
    print("Your name is ok.")