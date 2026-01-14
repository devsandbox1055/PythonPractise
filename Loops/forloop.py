# sum of number in a list
number   = [2,4,6,8]
total  = 0

for num in number:
    total  += num

print("sum  =" , total )

#count vowel in a string
word = "programming"
vowels = "aeiou"
count  = 0

for ch in word:
    if ch in vowels:
        count += 1

print("vowels  = " , count)