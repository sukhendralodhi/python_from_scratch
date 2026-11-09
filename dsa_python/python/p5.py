
a = 20
b = 6

print(a+b)
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)




age = 28
experience = 3

print(age > 18)          # Output: True
print(experience == 3)   # Output: True
print(age < 25)          # Output: False
print(experience != 2)   # Output: True



age = 25
has_python_knowledge = True
has_ai_knowledge = False

# 1. Both conditions must be True
print(age >= 18 and has_python_knowledge)  # Output: True

# 2. At least one condition must be True
print(has_python_knowledge or has_ai_knowledge)  # Output: True

# 3. Inverts the boolean value
print(not has_ai_knowledge)  # Output: True


skills = ["Python", "React", "FastAPI", "PostgreSQL"]

print("Python" in skills)

print("Java" in skills)

print("FastAPI" in skills)

print("Java" not in skills)

user_age = 25
is_verified = True
has_subscription = False
is_admin = True

print(user_age >= 18)
print(is_verified)
print(has_subscription or is_admin)