# print("Hello World")

# def greet():
#     print("Hello World")

# def add_no_return(a,b):
#     return(a+b)

# result = add_no_return(10,20)
# print(result)

def get_min_max(numbers):
    return min(numbers), max(numbers)


low, high = get_min_max([4,7,1,9,2])
# print(low)
# print(high)

# def is_even(number):
#     if number % 2 == 0:
#         return ("Even number")
#     else:
#         return ("Odd number")

# result = is_even(3)
# print(result)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


result = is_even(3)
if result:
    print("Even number")
else:
    print("Odd number")