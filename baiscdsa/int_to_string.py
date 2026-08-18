def int_to_string(number):

    digits = "0123456789"
    result = ""

    if number == 0:
        return "0"

    while number > 0:
        num = number % 10
        result = digits[num] + result
        number = number // 10

    return result


print(int_to_string(12377669))
print(type(int_to_string(123)))
