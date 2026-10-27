def find_max(numbers):
    largest_number = numbers[0]

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


result = find_max([1, 4, 9, 12, 7, 18])
print(result)



# fibonicci series 

def fib(num):

    if num ==0:
        return 1

    if num == 1: 
        return 1

    last = fib(num-1)
    secondLast = fib(num-2)

    return last + secondLast


print(fib(5))