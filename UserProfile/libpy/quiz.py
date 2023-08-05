from kivy.uix.screenmanager import ScreenManager
import time
import threading
import signal
from kivy.uix.screenmanager import Screen

class Quiz(Screen):
        def timeout_handler(signum, frame):
            raise TimeoutError

        def ask_question(question, choices, correct_answer, timeout):
            print(question)
            for idx, choice in enumerate(choices):
                print(f"{idx + 1}. {choice}")

            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

            try:
                user_choice = int(input("Your answer (enter the number): "))
                signal.alarm(0)  # Reset the alarm
            except (ValueError, TimeoutError):
                user_choice = None
                print("\nTime's up!\n")

            return user_choice == correct_answer

        def run_quiz():
            questions = [
                {
                    'question': 'What is the capital of France?',
                    'choices': ['Paris', 'London', 'Berlin'],
                    'correct_answer': 1,
                },
                {
                    'question': 'Which planet is closest to the sun?',
                    'choices': ['Venus', 'Mercury', 'Mars'],
                    'correct_answer': 2,
                },
                # Add more questions
            ]

            total_questions = len(questions)
            score = 0
            timeout = 10  # Time limit for each question in seconds

            for idx, q in enumerate(questions):
                print(f"\nQuestion {idx + 1}/{total_questions}:")
                if ask_question(q['question'], q['choices'], q['correct_answer'], timeout):
                    print("Correct!\n")
                    score += 1
                else:
                    print("Time's up or Incorrect!\n")

            print(f"Quiz completed! Your score: {score}/{total_questions}")

            pass