string = input()
countUpper = 0
countLower = 0
for i in range(len(string)):
    if string[i].isupper():
        countUpper += 1
    elif string[i].islower():
        countLower += 1

print(countUpper)
print(countLower)
