def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")

    # Loop through each line in the file like a list
    for line in my_file:
        print(line)


main()
