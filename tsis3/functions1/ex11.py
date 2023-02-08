def palindrome(word):
    x = 0
    n = int(len(word) / 2) + 1
    for i in range(int(len(word)/2)):
            if word[i] != word[len(word)-1-i]:
                print("false")
                break
            else:
                x+=1
    if x == int(len(word) / 2):
        print("true")
word = input()
palindrome(word)

