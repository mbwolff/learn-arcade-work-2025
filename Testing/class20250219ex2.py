def sum_print(a, b):
    """This function prints a sum"""
    result = a + b
    print(result)

def sum_return(a, b):
    """This function return a sum"""
    result = a + b
    return result

# This will return the result of the function
# and assign it to the variable 'result'
# The print happens outside the function
result = sum_return(4, 3)

# This will print the sum from inside a function
# I defined.
sum_print(5, 6)
