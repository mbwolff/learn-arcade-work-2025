def f(level):
    # Print the level we are at
    print("Recursion call, level",level)
    # If we haven't reached level ten...
    if level < 10:
        # Call this function again
        # and add one to the level
        f(level+1)
    print("End of recursion call, level", level)


# Start the recursive calls at level 1
f(1)
