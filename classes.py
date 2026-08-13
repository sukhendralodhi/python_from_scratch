# Step 12: Classes & Objects (OOP Basics)

# This is a big one — Object-Oriented Programming. It lets you bundle data and behavior together into reusable blueprints called classes.

class Dog:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread


    def bark(self):
        print(f"{self.name} says Woof!")


# dog1 = Dog("Rex", "Labrador")
# dog2 = Dog("Buddy", "Poodle")

# print(dog1.name)    # Rex
# print(dog2.bread)   # Poodle

# dog1.bark()   # Rex says Woof!
# dog2.bark()   # Buddy says Woof!


class BankBalance:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -=  amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print("Your current balance: ", self.balance)


# account = BankBalance("Alice", 400)
# account.check_balance()
# account.deposit(400)
# account.check_balance()
# account.withdraw(400)
# account.check_balance()


class Car:
    def __init__(self, brand, model, speed = 0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(self.speed)

    def brake(self, amount):
        if amount > self.speed:
            self.speed = 0
            print("Speed can not be negative, set to 0")
        else:
            self.speed -= amount
            print(self.speed)


car = Car("Toyota", "Corolla")
car.accelerate(50)   # speed = 50
car.brake(20)        # speed = 30  ✅ correct
car.brake(100)       # speed = 0, "Speed can not be negative, set to 0"  ✅ correct     # what should happen?