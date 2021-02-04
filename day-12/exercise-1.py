def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("Divisor cannot be zero.")
        return

    return x/y


print(add(2,2))
print(subtract(4,2))
print(multiply(2,2))
print(divide(4,0))
print(divide(0,4))