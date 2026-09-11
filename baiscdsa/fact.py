# def check_factorial(number):

#     if number == 0:
#         return 1

#     else:
#         return number * check_factorial(number - 1)


# factorialValue = check_factorial(5)
# print(factorialValue)


def check_factorial(number):

    fact = 1
    if number == 0:
        return 1

    
    while number > 0:
        fact = fact * number
        number = number-1

    return fact


factorialValue = check_factorial(0)
print(factorialValue)