import random
import time

class Quiz:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": "Paris",
            "Which planet is known as the Red Planet?": "Mars",
            "What is the chemical symbol for water?": "H2O",
            "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
            "What is the tallest mammal in the world?": "Giraffe"
        }
        self.score = 0
        self.total_questions = len(self.questions)
        self.time_limit = 10  # Time limit for each question in seconds

    def start_quiz(self):
        print("Welcome to the Quiz!")
        input("Press Enter to start...")
        self.ask_questions()
        self.display_score()

    def ask_questions(self):
        question_keys = list(self.questions.keys())  # Convert dictionary keys to a list
        for question in random.sample(question_keys, self.total_questions):
            print("\n" + question)
            start_time = time.time()
            answer = input("Your answer: ")
            elapsed_time = time.time() - start_time

            if elapsed_time > self.time_limit:
                print("Time's up!")
            elif answer.lower() == self.questions[question].lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

    def display_score(self):
        print("\nQuiz finished!")
        print("Your score:", self.score, "/", self.total_questions)

    def restart_quiz(self):
        self.score = 0
        self.start_quiz()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
    while True:
        choice = input("\nDo you want to restart the quiz? (yes/no): ")
        if choice.lower() == "yes":
            quiz.restart_quiz()
        elif choice.lower() == "no":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
