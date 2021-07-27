import random
number = random.randint(1, 20)
guess = int( input('guess a number between 1 and 20: '))
while guess!=number:
    if guess < number:
        guess = int( input('too low, guess again: ') )
    else:
        guess = int( input('too high, guess again: '))
print('Correct!')
