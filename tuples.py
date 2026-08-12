# Tuples like list, but immutable (cannot be changed after creation)

# cordinates = (10,20)
# print(cordinates)
# person = ("Alice", 20, "Engineer")
# print(person)

# why use a tuple instead of list
# 1. when data should not change (fixed cordinates, date etc)
# 2. tuples are slightly faster and use less memory than lists
# 3. they signal intent to others developers "this data is fixed"

person = ("Alice", 20, "Engineer")
# unpacking tuples 
name, age, job = person
print(name)
print(age)
print(job)