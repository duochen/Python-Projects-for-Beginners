from Homework6 import Quiz
import unittest

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.quiz = Quiz()
        self.quiz.questions = [
            {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"},
            {"question": "What is 2 + 2?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "answer": "B"},
        ]
    
    def test_correct_answer(self):
        self.quiz.ask_question({"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"})
        self.assertEqual(self.quiz.score, 1)
    
    def test_incorrect_answer(self):
        self.quiz.ask_question({"question": "What is 2 + 2?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "answer": "B"})
        self.quiz.ask_question({"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"})
        self.assertEqual(self.quiz.score, 2)

if __name__ == "__main__":
    unittest.main()
