def print_backwards(string):
    if len(string) > 0:
        print(string[-1], end="")
        print_backwards(string[:(len(string)-1)])
    else:
        print()


print_backwards("mushroom")
