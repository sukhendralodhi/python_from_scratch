class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi, {self.name} your avg score is: {sum/3}")


# s1 =  Student("Tony Stark", [98,99,97])
# s1.get_avg()


# abstraction
# Hiding the implementation details and showing only the functionality to the user is called abstraction. It can be achieved by using abstract classes and methods.


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def accelerate(self):
        self.clutch = True
        self.acc = True
        print("Car is accelerating")

    # @staticmethod
    # def greet():
    #     print("Hello")


c1 = Car()
c1.accelerate()


# Encapsultaion
# Wrapping the data and code together into a single unit is called encapsulation. It can be achieved by using private variables and methods.
