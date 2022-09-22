from re import S


operators = ['addition', 'subtraction', 'division', 'multiplication', 'square']
def get_input(operators):
        operation = input('Operation? (addition, subtraction, division, multiplication, square.) q for quit.\n>>')
        if operation.lower() == 'q':
            print('quitting...')
            quit()
        elif operation.lower() in operators:
            operation = operation.lower()
            return operation
        else:
            print('invalid, try again')
            get_input(operators)

def get_numbers(operation, operators):
    while True:
        try:
            if operation in operators[0:4]:
                x = int(input('number one\n>>'))
                y = int(input('number two\n>>'))
                break
            else:
                x = int(input('number to be squared\n>>'))
                y = 0
                break
        except ValueError:
            print('value error.')
            
    return x, y

def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def division(x, y):
    return x // y
def multiplication(x, y):
    return x * y
def square(x):
    return x * x

def math(operation, operators,):
    result = 0
    x, y = get_numbers(operation, operators)
    if operation == operators[0]:
        result = addition(x, y)
    elif operation == operators[1]:
        result = subtraction(x, y)
    elif operation == operators[2]:
        result = division(x, y)
    elif operation == operators[3]:
        result = multiplication(x, y)
    elif operation == operators[4]:
        result = square(x)
    return result

if __name__ == '__main__':
    while True:
        operation = get_input(operators)
        result = math(operation, operators)
        print(f'your result is...\n\n{result}')