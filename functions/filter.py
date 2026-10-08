def even(item):

    if item % 2 == 0:
        return True

    return False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

new_list = list(filter(even, lst))

# print(new_list)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

greater_than_five = list(filter(lambda x: x > 5, numbers))

# print(greater_than_five)


names = ["mohan", "deepak", "kajal", "rajveer"]

names_filter = list(filter(lambda n: len(n) > 5, names))

# print(names_filter)


even_greater_than_five = list(filter(lambda x: x % 2 == 0 and x > 5, numbers))

print(even_greater_than_five)
