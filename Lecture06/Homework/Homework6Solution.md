## Step-by-Step Guide: Debugging and Testing a Quiz Application in Python

This guide will help students implement, debug, and test a simple quiz application step by step. It includes clear explanations, code snippets, and troubleshooting techniques.

---

### **Step 1: Create a Basic Quiz Application**
Students will first implement a simple multiple-choice quiz in Python.

#### **1.1 Define the Quiz Data Structure**
- Use a list of dictionaries to store questions, options, and correct answers.

```python
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]
```

#### **1.2 Implement the Quiz Logic**
- Display questions one by one.
- Collect the user’s answer.
- Compare it with the correct answer and keep track of the score.

```python
def run_quiz():
    score = 0
    for q in quiz_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score}/{len(quiz_questions)}.")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
```

---

### **Step 2: Introduce Bugs**
To make students practice debugging, we introduce common errors in the code.

#### **2.1 Example Bugs**
1. **Incorrect Scoring**: The score does not increase when the answer is correct.
2. **Flawed Input Handling**: If a user enters lowercase input (e.g., "b"), it should still be considered correct.
3. **Missing Option Display**: Options are not shown correctly.
4. **Crash on Invalid Input**: If the user enters an unexpected response (e.g., "X"), the program may crash.

#### **2.2 Introduce the Bugs**
Modify the original code to contain errors:

```python
def run_quiz_with_bugs():
    score = 0
    for q in quiz_questions:
        print("\n" + q["question"])
        # BUG 1: Missing option display
        # for option in q["options"]:
        #    print(option)  (This line is mistakenly commented)

        user_answer = input("Enter your answer (A/B/C/D): ")  # BUG 2: No .strip().upper()

        if user_answer == q["answer"]:  # BUG 3: Should be user_answer.upper()
            print("Correct!")
            # BUG 4: Score is not incremented
            # score += 1  (This line is mistakenly removed)
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score}/{len(quiz_questions)}.")  # This will always be 0

if __name__ == "__main__":
    run_quiz_with_bugs()
```

---

### **Step 3: Write Test Cases**
Students will write test cases using Python’s `unittest` module.

#### **3.1 Install and Import unittest**
Python’s built-in `unittest` module will be used.

```python
import unittest
```

#### **3.2 Write Unit Tests**
Break the quiz into testable functions. First, modify the quiz to separate logic:

```python
def check_answer(user_answer, correct_answer):
    return user_answer.strip().upper() == correct_answer

def calculate_score(answers, correct_answers):
    score = 0
    for user, correct in zip(answers, correct_answers):
        if check_answer(user, correct):
            score += 1
    return score
```

Now write test cases:

```python
class TestQuiz(unittest.TestCase):

    def test_check_answer_correct(self):
        self.assertTrue(check_answer("C", "C"))
        self.assertTrue(check_answer(" c ", "C"))  # Case and space insensitive

    def test_check_answer_incorrect(self):
        self.assertFalse(check_answer("A", "C"))

    def test_calculate_score(self):
        user_answers = ["C", "B", "B"]
        correct_answers = ["C", "B", "B"]
        self.assertEqual(calculate_score(user_answers, correct_answers), 3)

        user_answers = ["A", "B", "C"]
        self.assertEqual(calculate_score(user_answers, correct_answers), 1)

if __name__ == "__main__":
    unittest.main()
```

---

### **Step 4: Debug the Application**
Students now debug the introduced issues by following these steps.

#### **4.1 Identify the Issues**
- Run the buggy version of the quiz and note incorrect behavior.
- Check which part of the code is responsible.

#### **4.2 Fix the Bugs**
- **Bug 1 (Options Not Displaying)**: Restore the loop that prints options.
- **Bug 2 (Case Sensitivity Issue)**: Add `.strip().upper()` to user input.
- **Bug 3 (Incorrect Answer Check)**: Ensure case sensitivity handling.
- **Bug 4 (Score Not Updating)**: Restore `score += 1` in correct answer logic.

```python
def run_fixed_quiz():
    score = 0
    for q in quiz_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1  # FIXED BUG

        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score}/{len(quiz_questions)}.")  # FIXED BUG

if __name__ == "__main__":
    run_fixed_quiz()
```

---

### **Final Notes**
- **Encourage students to use print statements** (`print(variable)`) to debug.
- **Introduce debugging tools** like `pdb`:
  ```python
  import pdb; pdb.set_trace()
  ```
- **Run the tests** after fixing bugs to confirm correctness:
  ```sh
  python -m unittest quiz_test.py
  ```