my_list = []

for i in range(5):
    user_input = input("Enter an integer: ")
    user_input = int(user_input)
    my_list.append(user_input)
    my_total = 0
    for number in my_list:
        my_total = my_total + number
    print(my_total)
