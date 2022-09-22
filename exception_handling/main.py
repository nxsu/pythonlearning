try:
    a = 20
    b = 5
    print(a/b)
except ZeroDivisionError:
    print('There is divide by zero error.')
finally:
    print('This is going to execute no matter what.')