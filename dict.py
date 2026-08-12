# dict = {
#     "name": "mohan",
#     "age": 20,
#     "address": "Indore"
# }

# print(dict)

# print(dict["name"])

# dict["age"] = 27
# print(dict["age"])

# dict["city"] = "Bhopal"

# print(dict["city"])

# del dict["city"]

# print(dict)

person = {
    "name": "Alice",
    "age": 25,
    "job": "Engineer"
}

# print(person("email"))
# print(person.get("email"))

# print(person.get("email", "Not provided"))

# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key, ":",value)

# if "city" in person:
#     print("Key exists")
# else:
#     print("Not found")

students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85}
]

# print(students)

# for student in students:
#     print(student.get("age"))

# data = {
#     "title": "React JS",
#     "author": "Facebook",
#     "year": 2003
# }

# for key, value in data.items():
#     print(value)

data = {
    "title": "React JS",
    "author": "Facebook",
    "year": 2003
}

print(f"{data['title']} by {data['author']}, published in {data['year']}")