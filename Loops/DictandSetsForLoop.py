students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
}

for student in students:     
    print(student)         

for student in students.keys():
    print(student)

#upar ke dono ways se print hota hai

#is waale se tareeke se value waala side bhi access ho jaayega

for student in students:
    print(student , "-" , students[student])

#agar alag se value pair ko access 
# karna hai to ye use kar sakte hai


for student in students.values():  
    print(student)

#agar dono ko ek saath access karna hai to
#aise karenge

for student , num in students.items():
    print(student, " -" , num)   



#FOR SETS ITERATION

tools = {"Django", "Flask", "pandas", "NumPy"}
for tool in tools:
    print(tool)

"""As you can see, the loop goes through 
the elements of your set in a different 
order than they were inserted. So, you can’t 
rely on the order of the elements when 
traversing sets in Python."""