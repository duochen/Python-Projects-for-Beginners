import random

def check(guess, correct_option, options):
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == correct_option:
            print('Correct!')
            score += 1
            still_guessing = False
        else:
            attempt += 1
            if attempt < 3:
                guess = input(f'Uh oh! Try again. Attempt {attempt + 1} of 3: ')
            else:
                print(f'Sorry, you\'ve used all your attempts. The correct answer is: {options[correct_option]}')
                still_guessing = False

score = 0
print('Welcome to the Ultimate Game of Trivia! Please answer by typing the option letter (a, b, c, or d).')

# List of questions with corresponding answers
questions = [
    {
        'question': 'Where is the Bermuda Triangle located?',
        'options': {'a': 'pacific ocean', 'b': 'atlantic ocean', 'c': 'indian ocean', 'd': 'mediterranean ocean'},
        'answer': 'b'
    },
    {
        'question': 'On average, what is the thing that Americans do 22 times a day?',
        'options': {'a': 'brush their teeth', 'b': 'read a book', 'c': 'look up', 'd': 'open the fridge'},
        'answer': 'd'
    },
    {
        'question': 'What kind of doctor invented cotton candy?',
        'options': {'a': 'cardiologist', 'b': 'pediatrician', 'c': 'dentist', 'd': 'doctor seuss'},
        'answer': 'c'
    }
]

# Shuffle the questions
random.shuffle(questions)

# Ask the questions in a random order
for q in questions:
    # Display the question and options
    print(f"{q['question']}")
    for option, text in q['options'].items():
        print(f"{option}: {text}")
    
    guess = input('Your answer (a, b, c, or d): ').lower()
    check(guess, q['answer'], q['options'])

print('Your Final Score in the Ultimate Game of Trivia is:', score)
