def main():
    """ Read in lines from a file """

    # Open file, and automatically close when we exit this block.
    with open("super_villains.txt") as my_file:

        # Loop through each line in the file like a list
        for line in my_file:
            line = line.strip()
            print(line)


main()
