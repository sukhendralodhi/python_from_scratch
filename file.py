# with open("notes.txt", "w") as file:
#     file.write("hello this is a note")

# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())