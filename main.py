from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

# Define the quiz questions and answers
questions = [
    {
        "question": "Is Python a programming language?",
        "answer": True,
    },
    {
        "question": "Is Android an operating system?",
        "answer": True,
    },
    {
        "question": "Is HTML a programming language?",
        "answer": False,
    },
]


class QuizApp(MDApp):
    def build(self):
        self.index = 0
        self.dialog = None
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("quiz.kv")

    def show_next_question(self):
        if self.index < len(questions):
            self.show_question(questions[self.index])
            self.index += 1
        else:
            self.show_result()

    def show_question(self, question):
        self.dialog = MDDialog(
            title=question["question"],
            buttons=[
                MDRaisedButton(text="YES", on_release=self.check_answer),
                MDRaisedButton(text="NO", on_release=self.check_answer),
            ],
        )
        self.dialog.open()

    def check_answer(self, instance):
        answer = instance.text == "YES"
        correct_answer = questions[self.index - 1]["answer"]
        self.dialog.dismiss()

        if answer == correct_answer:
            title = "Correct!"
        else:
            title = "Incorrect!"

        self.dialog = MDDialog(title=title, text=f"The answer is {correct_answer}.")
        self.dialog.open()

        self.show_next_question()

    def show_result(self):
        correct_answers = sum(question["answer"] for question in questions)
        total_questions = len(questions)
        result = f"You scored {correct_answers} out of {total_questions} questions correctly."
        self.dialog = MDDialog(title="Quiz Result", text=result)
        self.dialog.open()


if __name__ == "__main__":
    QuizApp().run()
