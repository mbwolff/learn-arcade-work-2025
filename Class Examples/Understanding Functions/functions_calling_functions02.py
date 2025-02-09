# Example 2
def a():
    b()
    print("A")


def b():
    c()
    print("B")


def c():
    print("C")


a()