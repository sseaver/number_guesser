import random

print ("Think of a number between 1 and 100 for the computer to guess")

my_number = input("What is your number?")
my_number = int(my_number)
guesses = 0
low = 0
high = 100
computer_guess = random.randint(low, high)
print ("Computer guess = ", computer_guess)

while computer_guess != my_number and guesses < 5:
    if computer_guess < my_number:
        print ("The computer has guessed too low.")
        low = computer_guess + 1
    elif computer_guess > my_number:
        print ("The computer has guessed too high.")
        high = computer_guess - 1
    else:
        print ("The computer has guessed your number.")
    guesses += 1
    computer_guess = random.randint(low, high)
    print (computer_guess)

if guesses == 5 and computer_guess != my_number:
    print ("Congrats! You have stumped the computer!")
else:
    print ("The computer has guessed your number.")
