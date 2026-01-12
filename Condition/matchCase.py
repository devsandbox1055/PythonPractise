#Ek value ke base pe multiple conditions
#ko clean tareeke se handle karna

#USEAGE
#Jab ek variable ho
#Aur uske multiple fixed options ho
#Tab if–elif se zyada clean & readable hota hai


#EXAMPLE -1

#DAY OF WEEK

day = int(input("Enter day number (1-7): "))

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
        print("Invalid day")
