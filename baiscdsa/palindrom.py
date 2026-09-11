# def check_palindrom(value):
#     newValue = ""
#     for char in reversed(value):
#         newValue += char
#     print(newValue)
#     return newValue == value


# isPalindrom = check_palindrom(121)
# print(isPalindrom)
# # check_palindrom("hello")

def check_palindrom(value):
    original = value
    reversed_number = 0

    while value > 0:
        digit = value % 10
        reversed_number = reversed_number * 10 + digit
        value = value // 10

    return original == reversed_number


isPalindrom = check_palindrom(121)
print(isPalindrom)
