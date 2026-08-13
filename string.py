# text = "Hello World"
# name = "sukhendra singh lodhi"

# print(text.upper())
# print(text.lower())
# print(name.title())
# print(name.capitalize())

# Whitespace & cleaning

# text1 = "   Hello World   "
# print(text1)
# print(text1.strip())
# print(text1.lstrip())
# print(text1.rstrip())

# Searching & checking
# text = "Hello World"

# print(text.find("World"))
# print("World" in text)
# print("Sanju" in text)
# print(text.startswith("Hello"))
# print(text.startswith("Sanju"))
# print(name.endswith("lodhi"))
# print(name.endswith("Hello"))
# print(text.count("o"))
# print(name.count("o"))

# Replacing

# text = "I like cats"
# new_text = text.replace("cat", "dog")
# print(new_text)


# Splitting and joining

# text = "apple,banana,cherry"
# fruits = text.split(",")
# print(fruits)

# sentence = "This is Python"
# words = sentence.split()
# print(words)

# fruits = ["apple", "banana", "cherry"]
# joined = ", ".join(fruits)
# print(joined)


# Checking string content


# print("123".isdigit())
# print("abc".isalpha())
# print("abc123898#$%^&".isalnum())
# print(" ".isspace())

text = "Python"
# print(text[0]) # first value
# print(text[-1]) # last value
# print(text[0:3]) # from 0 to 2 bcz 2 is not include
# print(text[::-1]) # reverse the string

# f-strings, advanced formatting

# price = 4
# print(f"Price: ${price:.2f}")

# print(f"{'hello':>10}")  
# print(f"{'hello':<10}|")
# print(f"{42:05}")

# Important: strings are immutable

# text = "hello"
# text[0] = "H"   # ❌ TypeError! Can't modify a string in place

# text = "H" + text[1:]   # ✅ this creates a NEW string instead
# print(text)   # Hello


sentence = "  the Quick Brown fox  "
remove_whitespace = sentence.strip()
title = remove_whitespace.title()
words = title.split()
print(remove_whitespace)
print(title)
print(words)
print(len(words))