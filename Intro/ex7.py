# 7.	Write a function that takes 3 arguments.
# The first 2, "x" and "y" are numbers.
# The 3rd, "op" is a string that is one of "+", "-", "/", "*".
# Return the operation denoted by "op" computed on "x" and "y".
# E.g. If "op" is "+" return the sum of "x" and "y".
# HINT: Use "elif".

def select_operation(x, y, op):
    """
    Return the operation denoted by "op" computed on "x" and "y".
    E.g. If "op" is "+" return the sum of "x" and "y".
    """
    if op == '+':
        return str(x + y)
    elif op == '-':
        return str(x - y)
    elif op == '*':
        return str(x * y)
    elif op == '/':
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return str(x / y)
    else:
        raise ValueError('The operator must be one of: "+", "-", "*", "/".')

x = 12
y = 4
op = '*'
print('\n Exercise 7')
print(f' The result of {x} {op} {y} is {select_operation(x, y, op)}')