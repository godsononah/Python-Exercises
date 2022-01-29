# Guess the correct number
import random

print('I have picked a number from 0 through 9.\nCan you guess the number?\n')
number = random.choice(range(10))

while True:
    guess = int(input('Enter a number (0-9): '))

    if guess > number:
        print('Wrong! Guess is greater than the number.\n')
    elif guess < number:
        print('Wrong! Guess is less than the number.\n')
    else:
        break
print('Correct!')
