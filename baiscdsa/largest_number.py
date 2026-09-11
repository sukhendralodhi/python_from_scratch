def find_max(numbers):
    largest_number = numbers[0]

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


result = find_max([1, 4, 9, 12, 7, 18])
print(result)
