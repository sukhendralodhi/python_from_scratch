def count_digits(number):

    counter = 0

    if number == 0:
        return 1

    number = abs(number)

    while number > 0:
        temp = number % 10
        counter += 1
        number = number // 10

    return counter


print(count_digits(0))
