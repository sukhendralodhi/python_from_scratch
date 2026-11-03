

day = int(input("Enter day:"))

match day:

    case 1 | 2 | 3 | 4 | 5:
        print("Today is weekday")

    case 6 | 7:
        print("Today is weekend")

    case _:
        print("Please enter number between 1 to 7")