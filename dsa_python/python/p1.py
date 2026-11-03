

day = int(input("Pls enter the desired number: "))

if day == 0:
    print("Pls enter between 1 to 7")

match day:
    case 1:
        print("Monday")
    
    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Looking forward to the Weekend")