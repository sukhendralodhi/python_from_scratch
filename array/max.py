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


def reverse_to_new_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
        print(i)
    return reversed_arr


# print(reverse_to_new_list([2, 5, 6, 8, 4, 1, 9]))


def find_element(nums, target):

    for i in range(0, len(nums)):

        if target == nums[i]:
            return i

    return -1


# print(find_element([2, 5, 6, 8, 4, 1, 9], 1))


def count_occurrences(arr, target):

    count = 0

    for i in range(0, len(arr)):

        if target == arr[i]:
            count = count + 1

    return count


# print(count_occurrences([1, 2, 2, 3, 2, 4], 6))


def is_sorted(arr):

    if len(arr) <= 1:
        return True

    for i in range(len(arr) - 1):

        if arr[i] > arr[i + 1]:
            return False

    return True


# print(is_sorted([1, 2, 5, 8]))


def second_largest(arr):

    largest = arr[0]
    second = arr[1]

    for i in range(2, len(arr)):

        if largest > arr[i]:

            second = largest
            largest = arr[i]

        elif arr[i] > second:
            second = arr[i]

    return second


print(second_largest([10, 5, 20, 8, 15]))
