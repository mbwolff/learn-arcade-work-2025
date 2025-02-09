# Example 12
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
x2, y2 = a(x, y) # Most computer languages don't support this

print(x2)
print(y2)