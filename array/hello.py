import random
import string

# Password of your TEST network
target_password = "Airtel_abhi_8023"

characters = string.ascii_letters + string.digits

attempts = 0

while True:
    password = "".join(random.choices(characters, k=6))
    attempts += 1

    print(f"Attempt {attempts}: {password}")

    if password == target_password:
        print(f"\nPassword found: {password}")
        print(f"Attempts: {attempts}")
        break
