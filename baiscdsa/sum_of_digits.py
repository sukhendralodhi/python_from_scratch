def sum_of_digits(number):

    sum = 0

    if number < 0:
        return 0

    while number > 0:
        temp = number % 10
        sum += temp
        number = number // 10

    return sum


print(sum_of_digits(1237))
