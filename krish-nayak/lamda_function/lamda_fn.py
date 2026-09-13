# lambda function
# lambda function: A lambda function is a small anonymous function defined using the `lambda` keyword in Python. It can take any number of arguments but can only have one expression. The expression is evaluated and returned when the lambda function is called.


def addition(x, y):
    return x + y


# print(addition(5, 3))  # Output: 8

# lambda function syntax:

# lambda arguments: expression

addition_lambda = lambda x, y: x + y
print(addition_lambda(5, 3))  # Output: 8
print(type(addition_lambda))  # Output: <class 'function'>


def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

even_lambda = lambda num: num % 2 == 0
print(even_lambda(4))  # Output: True
print(even_lambda(5))  # Output: False

three_nums = lambda x, y, z: x + y + z
print(three_nums(1, 2, 3))  # Output: 6