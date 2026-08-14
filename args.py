# *args — collects any number of extra positional arguments into a tuple


def add_all(*numbers):
    print(numbers)
    return sum(numbers)


# print(add_all(1, 2, 3, 4))

# **kwargs — collects extra keyword arguments into a dictionary


def describe_person(**values):
    print(values)  # kwargs is a dict


# describe_person(name="Alice", age=25, job="Engineer")
# {'name': 'Alice', 'age': 25, 'job': 'Engineer'}


def add(a, b, c):
    return a + b + c


numbers = [1, 2, 3]

# print(add(*numbers))


info = {"a": 1, "b": 2, "c": 3}
# print(add(**info))


def total_price(*numbers):
    return sum(numbers)


print(total_price(1, 2, 3, 4))
print(total_price(4, 8, 9, 5, 5))
print(total_price(4, 8, 9, 5, 5, 3, 2, 1))
