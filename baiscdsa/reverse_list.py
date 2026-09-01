def reverse_list(list):
    new_list = []

    for item in list:
        new_list.insert(0, item)

    return new_list


print(reverse_list([1, 2, 3, 4, 5]))
