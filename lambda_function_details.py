numbers = [3, 1, 2]
# print(sorted(numbers))


students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]


# print(sorted(students))
# def get_score(student):
#     return student[1]


# sorted_students = sorted(students, key=get_score, reverse=True)
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_students)
