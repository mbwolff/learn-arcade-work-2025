from random import randint

# --- Binary search
biggest_possible_number = 512
magic_number = randint(1, biggest_possible_number)
lower_bound = 0
upper_bound = biggest_possible_number + 1
found = False

print(f"The magic number is {magic_number} with an upper limit of {biggest_possible_number}.")
print("How many guesses does the computer need?")

guesses = []
guess = None

# Loop until we find the number, or our upper/lower bounds meet
while lower_bound < upper_bound and not found:
    # Guess the middle position
    guess = (lower_bound + 1) + ((upper_bound - 1) - (lower_bound + 1)) // 2
    guesses.append(guess)
    print(f"U: {upper_bound}, L: {lower_bound}, G: {guess}")
    # Figure out if we:
    # move up the lower bound, or
    # move down the upper bound, or
    # we found what we are looking for
    if guess < magic_number:
        lower_bound = guess
    elif guess > magic_number:
        upper_bound = guess
    else:  # guess == magic_number
        found = True

print(f"The computer finally guessed {guess}.")
print(f"The computer guessed {len(guesses)} times.")
