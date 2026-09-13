numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[2:5]) # this will return items from index 2 to 4
# print(numbers[5:]) # this will return all the items from index 5 to end
# print(numbers[:5]) # this will return all the items from start to index 4
# print(numbers[::2])  # this will return every second item from the list
# print(numbers[::-1])  # this will return the list in reverse order


# list comprehension is a concise way to create lists in Python. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

# Basic
# [expression for item in iterable]

# With condition
# [expression for item in iterable if condition]

squares = [x**2 for x in range(10)]
# print(squares)

lst = []

for i in range(10):
    if i % 2 == 0:
        lst.append(i)

# print(lst)

even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)


list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

pair = [[x, y] for x in list1 for y in list2]
print(pair)

words = ['hello', 'world', 'python', 'programming']
lengths = [len(word) for word in words]
print(lengths)

# comprehension with else
result = [x if x % 2 == 0 else 'hello' for x in range(10)]
print(result)