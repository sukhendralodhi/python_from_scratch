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

# print(even_greater_than_five)

people = [
    {"name": "Sukhendra", "age": 26},
    {"name": "Somakshi", "age": 20},
    {"name": "Gautam", "age": 35},
    {"name": "Kajal", "age": 18},
]


def check_age(person):

    return person["age"] > 25


res = list(filter(check_age, people))

# print(res)

result = list(filter(lambda person: person["age"] > 18, people))

print(result)
