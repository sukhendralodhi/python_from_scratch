def find_max(nums):
    max = nums[0]

    for x in nums:
        if x > max:
            max = x

    return max


# print(find_max([2,5,6,8,4,9,10,30]))  # Output: 9


def find_min(nums):
    min = nums[0]

    for i in range(0, len(nums)):

        if nums[i] < min:
            min = nums[i]

    return min


# print(find_min([2, 5, 6, 8, 4, 1, 9, 10, 30]))  # Output: 9


def array_sum(nums):

    sum = 0

    for i in range(0, len(nums)):

        sum = sum + nums[i]

    return sum


# print(array_sum([2, 5, 6, 8, 4, 1, 9]))


def count_even(nums):

    even_number = 0

    for i in range(0, len(nums)):

        if nums[i] % 2 == 0:
            even_number += 1

    return even_number


# print(count_even([2, 5, 6, 8, 4, 1, 9]))


def reverse_array(nums):

    return nums[::-1]


# print(reverse_array([2, 5, 6, 8, 4, 1, 9]))


def reverse_array1(nums):

    for i in range(len(nums), 0):
        print(nums[i])


print(reverse_array1([2, 5, 6, 8, 4, 1, 9]))
