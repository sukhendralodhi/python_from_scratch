# try:
#     number = int(input("Enter the number: "))
#     print(f"You entered {number}")
# except ValueError:
#     print("That is not a valid number")


# ValueError      # wrong type of value, e.g. int("abc")
# ZeroDivisionError  # dividing by zero
# TypeError       # wrong type used in an operation, e.g. "5" + 5
# KeyError        # accessing a dict key that doesn't exist
# IndexError      # accessing a list index that doesn't exist
# FileNotFoundError  # trying to open a file that doesn't exist


# try:
#     result = 10 / int(input("Enter a divisor: "))
#     print(result)
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("Can not divided by zero")

# try:
#     number = int(input("Enter the number: "))
# except ValueError:
#     print("Invalid input")
# else:
#     print(f"Success! You entered {number}")
# finally:
#     print("Done processing")

def risky_code():
    print("Hello World")

try:
    risky_code()
except Exception as e:
    print(f"Something went wrong: {e}")