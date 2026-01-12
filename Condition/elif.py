# multiple condition ko top-down check karta hai
# Ek condition true hote hi baaki skip ho jaati hain.
marks  = int(input("enter your marks"))

if marks >= 90:
    print("grade A")
elif marks >= 70:
    print("grade b")
elif marks >=40:
    print("grade c")
else:
    print("failed")


#EXAMPLE -2
#DAY OF WEEK

# Print day name using number

day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")


# SIMPLE CALCULATOR

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")


#elif tab use hota hai jab multiple 
# conditions ho aur sirf ek hi 
# execute karna ho.