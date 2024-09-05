class Quiz:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"},
            {"question": "What is 2 + 2?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "answer": "B"},
        ]
        self.score = 0

    def ask_question(self, q):
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Choose the correct option (A, B, C, D): ").strip().upper()
        if answer == q["answer"]:
            self.score += 1
            print("Correct!")
        else:
            print("Wrong answer.")

    def start(self):
        for q in self.questions:
            self.ask_question(q)
        print(f"Your final score is: {self.score}/{len(self.questions)}")

# To run the quiz
if __name__ == "__main__":
    quiz = Quiz()
    quiz.start()
