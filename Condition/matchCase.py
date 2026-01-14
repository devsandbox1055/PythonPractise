#Ek value ke base pe multiple conditions
#ko clean tareeke se handle karna

#USEAGE
#Jab ek variable ho
#Aur uske multiple fixed options ho
#Tab if–elif se zyada clean & readable hota hai


#STRUCTURE
"""match value:
    case option1:
        # code
    case option2:
        # code
    case _:
        # default case   """


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


#SIMPLE CALCULATOR

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

match op:
    case "+":
        print("Result =", a + b)
    case "-":
        print("Result =", a - b)
    case "*":
        print("Result =", a * b)
    case "/":
        if b != 0:
            print("Result =", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operation")


