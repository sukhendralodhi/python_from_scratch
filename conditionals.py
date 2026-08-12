# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are an adult.")
# elif age >= 13:
#     print("You are a teenager.")
# else:
#     print("You are a child")

age = int(input("Enter your age: "))
has_id = input("Enter 1 or 0: ") == "1"
print(has_id)   # True if user typed "1", False otherwise

if age >= 18 and has_id:
    print("You can enter")

if age < 18 or not has_id:
    print("You can not enter")