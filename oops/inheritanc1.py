class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


dog = Dog("Rex", "Labrador")
print(dog.name)  # Rex  <- set by Animal's __init__ via super()
print(dog.breed)  # Labrador  <- set by Dog's own __init__

cat = Cat("Whiskers")
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True -- a Dog IS an Animal (inheritance relationship)
print(isinstance(cat, Dog))  # False
