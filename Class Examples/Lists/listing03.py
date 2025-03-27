# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Add element 0, next 1, then 2, etc.
    list_total += my_list[index]

# Print the result
print(list_total)
