import random

guesses = 0
computer_number = random.randint(1, 100)
my_guess = input("Guess the computer's number.")
my_guess = int(my_guess)
guesses += 1

while guesses < 5 and my_guess != computer_number:
    if my_guess > computer_number:
        print ("Too big. Try again.")
    elif my_guess < computer_number:
        print ("Too small. Try again.")
    if abs((my_guess - computer_number)) < 10:
        print ("You are within 10!")
    if abs((my_guess - computer_number)) < 3:
        print ("You are within 3!")
    my_guess = input("Guess again")
    my_guess = int(my_guess)
    guesses += 1

if guesses == 5 and my_guess != computer_number:
    print ("You are out of tries. Play again.")
    print ("My number was", computer_number)
else:
    print ("Way to go!")
