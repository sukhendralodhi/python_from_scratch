# lst = []
# print(type(lst))

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(fruits[0])  # Output: apple
# print(fruits[1])  # Output: banana
# print(fruits[2])  # Output: cherry
# print(fruits[3])  # Output: orange
# print(fruits[4])  # Output: kiwi
# print(fruits[5])  # Output: melon
# print(fruits[6])  # Output: mango

# print(fruits[-1])  # Output: mango

# print(fruits[1:]) # this will return all the items from list
# print(fruits[1:4]) # this will return items from index 1 to 3

# modifying the list
# fruits[1] = "blueberry"
# print(fruits)

# list methods

# append - this will add items to the end
fruits.append("papaya")
print(fruits)

# insert - this will add items to the specific index
# syntax - insert(index, item)

fruits.insert(0, "grapes")
print(fruits)

# remove - this will remove the first matching item from the list
# syntax - remove(item)

fruits.remove("kiwi")
print(fruits)

# pop - this will remove the item at the specified index and return it
# syntax - pop(index)
# this will return the last item if index is not specified

poped_item = fruits.pop(2)
print(fruits)
print(poped_item)


# want to find index of an item in the list
# syntax - index(item)
index_of_item = fruits.index("mango")
print(index_of_item)

counting_item = fruits.count("mango")
print(counting_item)
