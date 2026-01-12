# find largest among three numbers

a  = int(input("enter the first number"))
b  = int(input("enter the second number"))
c = int(input("enter the second number"))

if a >b:
    if a>c:
        print("a is the largest")
    else:
        print("c is the largest")
else:
    if b >c:
        print("b is the largest")
    else:
        print("c is the largest")


# login check using nested if


username  = input("enter username")
password = input("enter the password")

if username  == "admin":
    if password  == "1234":
        print("login sucessful")
    else:
        print("wrong password")
else:
    print("invalid password")

#even odd number checker

num  = int(input("enter a number"))

if num%2==0:
    print(num , "this number is even")
else:
    print("this number is negative")

