# set defination: A set is a collection of distinct objects, considered as an object in its own right. In Python, sets are defined using curly braces {} or the set() function. Sets are unordered, meaning that the items do not have a defined order, and they do not allow duplicate elements.

my_set = {1, 2, 3, 4, 5}
empty_set = set()  # this is how we can create an empty set

print(my_set)
print(type(my_set))

# basic sets operations

# adding items to the set
my_set.add(6)
print(my_set)

# removing items from the set
# my_set.remove(10)  # this will raise an error if the item is not present in the set
# print(my_set)

# how we can handle the error while removing an item from the set
try:
    my_set.remove(10)
except KeyError:
    print("Item not found in the set")

# discard method - this will remove the item from the set if it is present, otherwise it will do nothing
my_set.discard(10)
print(my_set)

# removing random item from the set
removed_item = my_set.pop()
print(my_set)
print(removed_item)