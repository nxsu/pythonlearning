def add_ten(x):
    return x + 10

def twice(func, argument):
    return func(func(argument))

number = 0

number = twice(add_ten, number)

print(number)