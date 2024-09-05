import random

# List of questions with multiple choice answers and the correct answer
questions = [
    {"question": "What is the capital of France?", "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"], "answer": "A"},
    {"question": "What is 2 + 2?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "answer": "B"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "answer": "B"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. Shakespeare", "B. Dickens", "C. Austen", "D. Orwell"], "answer": "A"},
]

def display_question(question_data):
    """Displays a question and its options, and gets the user's answer."""
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    return user_answer

def quiz_game():
    """Runs the interactive quiz game."""
    score = 0
    random.shuffle(questions)  # Shuffle questions to present them in random order
    
    for question in questions:
        user_answer = display_question(question)
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")
        print()  # Blank line for spacing
    
    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
