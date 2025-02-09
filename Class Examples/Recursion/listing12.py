def binary_search_recursive(search_list, key, lower_bound, upper_bound):
    middle_pos = (lower_bound + upper_bound) // 2
    if (middle_pos == lower_bound) or (middle_pos == upper_bound) or (lower_bound > upper_bound):
        print("Key not found!")
    elif search_list[middle_pos] < key:
        # Recursively search top half
        binary_search_recursive(search_list, key,
                                middle_pos + 1, upper_bound)
    elif search_list[middle_pos] > key:
        # Recursively search bottom half
        binary_search_recursive(search_list, key,
                                lower_bound, middle_pos )
    else:
        print("Found at position", middle_pos)


def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")

    # Create an empty list to store our names
    name_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        name_list.append(line)

    my_file.close()

    print("There were", len(name_list), "names in the file.")

    # --- Binary search
    key = "Vidar the Ogre"
    lower_bound = -1
    upper_bound = len(name_list)

    # Start the recursive search!
    binary_search_recursive(name_list, key, lower_bound, upper_bound)


main()
