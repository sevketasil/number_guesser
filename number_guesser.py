import random

preferred_max = input("Please type a number for the maximum value: ")
if preferred_max.isdigit():
    preferred_max = int(preferred_max)
    if preferred_max <= 1: 
        print("Please type a maximum value bigger than 1")
        quit()
else: 
    print("Please type an integer number")
    quit()

random_number = random.randint(0, preferred_max)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Please make a guess between 0 and " + str(preferred_max) + ": ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Please type an integer number")
        continue
    if user_guess == random_number:
        print("Congratulations, you found it!")
        break
    elif user_guess > random_number:
            print("Your guess was higher than the actual number")
    elif user_guess < random_number:
            print("Your guess was lower than the actual number")

print("You got it in " + str(guesses) + " guesses")