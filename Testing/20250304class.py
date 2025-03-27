for i in range(1, 10):
    for j in range(9 - i):
        print("  ", end="")
    for j in range(i):
        print(j + 1, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
for i in range(1, 9):
    # print spaces
    for j in range(i):
        print("  ", end="")
    for j in range(1, 10 - i):
        print(j, end=" ")
    print()