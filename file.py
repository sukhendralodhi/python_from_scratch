# with open("notes.txt", "w") as file:
#     file.write("hello this is a note")

# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("notes.txt", "a") as file:
#     file.write("\n Another note hello sanju")

# with open("notes.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# try:
#     with open("notes1.txt", "r") as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#     print("File not found!")

# try:
#     with open("notes.txt", "r") as file:
#         for line in file:
#             value = line.strip().split(",")
#             print(value)
# except FileNotFoundError:
#     print("File not found")


# with open("movies.txt", "w") as file:
#     file.write("Inception\n")
#     file.write("The Matrix\n")
#     file.write("Interstellar\n")


# with open("movies.txt", "r") as file:
#     for line in file:
#         print(line.strip())


with open("new_movies.txt", "w") as file:
    file.write("Captain America\n")
    file.write("Lokki\n")
    file.write("Avengers Endgame\n")


with open("new_movies.txt", "r") as file:
    for line in file:
        print(line.strip())