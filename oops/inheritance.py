# Inheritance lets one class reuse and extend another class's code, instead of rewriting everything from scratch. This is one of the most powerful ideas in OOP.

# without inheritance

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")

#     def make_sound(self):
#         print("Woof!")


# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")  # duplicated!

#     def make_sound(self):
#         print("Meow!")


# after inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print("Some generic animal sound!")


class Dog(Animal):
    def make_sound(self):
        print("Woof")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


dog = Dog("Rex")
cat = Cat("Whiskers")

dog.eat()  # Rex is eating.       <- inherited from Animal, not redefined
dog.make_sound()  # Woof!                <- Dog's own override

cat.eat()  # Whiskers is eating.  <- inherited too
cat.make_sound()  # Meow!
