def add_all(*args):
    print(args)
    return sum(args)

# print(add_all(1, 2, 3))        # (1, 2, 3) -> 6
# print(add_all(1, 2, 3, 4, 5)) 

def describe_person(**kwargs):
    print(kwargs)

describe_person(name="Alice", age=25, job="Engineer")

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=25, job="Engineer")
# name: Alice
# age: 25
# job: Engineer