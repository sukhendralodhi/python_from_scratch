# numbers = [1,2,3,4,5]
# squares = []

# for n in numbers:
#     squares.append(n ** 2)

# print(squares)

# numbers = [1,2,3,4,5]
# squares = [n ** 2 for n in numbers]
# print(squares)

# Same result, one line. The pattern is: [expression for item in iterable]

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evens = [n for n in numbers_list if n % 2 == 0]
# print(evens)

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# labels = ["even" if n % 2 == 0 else "odd" for n in numbers_list]
# print(labels)

# names = ["alice", "bob", "carol"]
# name_lengths = {name: len(name) for name in names}
# print(name_lengths)

words = ["apple", "banana", "kiwi", "fig", "orange"]
new_words = [n for n in words if len(n) > 4]

print(new_words)
