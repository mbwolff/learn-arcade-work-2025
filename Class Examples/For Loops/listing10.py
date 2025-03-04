# What is the value of sum?
#total = 0
#for i in range(1, 101):
#    total = total + i
#print(total)

total = 0
total_number_of_zeros = 0
for i in range(5):
    new_number = int(input( "Enter a number: "))
    total = total + new_number
    if new_number == 0:
        total_number_of_zeros += 1
print(total)
print("You entered", total_number_of_zeros, "zeros")
