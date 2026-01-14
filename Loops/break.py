"""The break statement immediately 
exits the loop and jumps 
to the first statement after the loop."""

numbers = [1, 3, 5, 7, 9]
target = 3

for number in numbers:
    print(f"Processing {number}...")
    if number == target:
        print(f"Target found {target}!")
        break