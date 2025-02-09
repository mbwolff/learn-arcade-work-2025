for i in range(1, 10):
    for j in range(9-i, 0, -1):
        print(" ", end=" ")
    for j in range(i):
        print(j+1, end=" ")
    for j in range(j, 0, -1):
        print(j, end=" ")
    print()
for i in range(9):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(1, 9-i):
        print(j, end=" ")
    for j in range(7-i, 0, -1):
        print(j, end=" ")
    print()

