import random
def game(name, guess, status):
    counter = 0
    while status == "guessing":
        trial = int(input("take a guess"))
        if trial > guess:
            print("your guess is too high")
            counter += 1
        elif trial < guess:
            print("your guess is to low")
            counter += 1
        elif trial == guess:
            counter += 1
            print("Good job," + name +"! You guessed my number in " + str(counter) + " guesses!")
            status = "guessed"

name = input("Hello! What is your name?")
status = "guessing"
guess = random.randint(1, 20)
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
counter = 0
game(name, guess, status)