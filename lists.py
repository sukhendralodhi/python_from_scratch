# fruits = ["apple", "banana", "cherry"]
# # numbers = [1,2,3,4,5,6,7,8]
# # mixed = ["hello", 42, True, 3.14] # list can hold mixed types
# # print(mixed)
# # print(numbers)
# # print(fruits)

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# numbers = [10,20,30,40,50,60,70]
# print(numbers[1:3])
# print(numbers[:2])
# print(numbers[2:])


# fruits = ["apple", "banana", "cherry"]
# fruits.append("Mango") # add in end
# fruits.remove("banana") # remove by value
# fruits.insert(0, "orange")
# fruits.pop() # remove last item 
# fruits[0] = "mango"
# print(fruits)

# useful list functions 



# print(len(numbers))
# print(sorted(numbers))
# print(numbers.sort())
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if "apple" in fruits:
        print("Apple found")
        break

# with index using enumerate()

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

numbers = [5,3,8,1]
result = numbers.sort()
print(result) # this will return None
print(numbers) # this print sorted array