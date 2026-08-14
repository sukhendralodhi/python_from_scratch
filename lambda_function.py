# A lambda is a small, anonymous (unnamed), one-line function — useful for short throwaway logic, especially when passed into other functions.


# Regular function
def square(number):
    return number**2


# print(square(4))

multipication = lambda x, y: x * y
# print(multipication(3, 4))


people = [("Alice", 25), ("Bob", 19), ("Carol", 28)]

sorted_people = sorted(people, key=lambda person: person[1])
# print(sorted_people)

numbers = [1, 2, 3, 4]
squared = list(map(lambda n: n**2, numbers))
# print(squared)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda n: n % 2 == 0, numbers))
# print(evens)  # [2, 4, 6, 8]


students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]

sorted_students = sorted(students, key=lambda student: student[0])
# print(sorted_students)


