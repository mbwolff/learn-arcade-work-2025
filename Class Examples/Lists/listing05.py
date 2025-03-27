# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
print(my_list)

# Loop from 0 up to the number of elements
# in the array:
for i in range(len(my_list)): # for i in range(9)
    my_list[i] = my_list[i] * 2

# Print the result
print(my_list)