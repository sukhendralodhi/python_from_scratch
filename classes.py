# Step 12: Classes & Objects (OOP Basics)

# This is a big one — Object-Oriented Programming. It lets you bundle data and behavior together into reusable blueprints called classes.

class Dog:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread


    def bark(self):
        print(f"{self.name} says Woof!")


dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Buddy", "Poodle")

print(dog1.name)    # Rex
print(dog2.bread)   # Poodle

dog1.bark()   # Rex says Woof!
dog2.bark()   # Buddy says Woof!