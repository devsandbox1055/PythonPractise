#for loops can have an else clause at the end. 
# The else clause will only run if the loop t
# erminates because of the exhaustion of the input 
# iterable

numbers = [1, 3, 5, 7, 9]
target  = 9

for number in numbers:
    print(f"processing{number}..")
    if number == target:
        print(f" Target found {target}")
        break
else:
    print(f"target not found {target}")