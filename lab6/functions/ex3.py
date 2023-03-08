string = input()

def is_pal(string):
    if list(string) == list(reversed(string)):
        return True
    else:
        return False

if is_pal(string):
    print("it's palindrome")
else:
    print("it's not")