def reverse_number(number):
    result = ""
    while number > 0:
        num = number % 10
        result = result + str(num)
        number = number // 10

    return int(result)


print(type(reverse_number(123456)))
print(reverse_number(87987))
