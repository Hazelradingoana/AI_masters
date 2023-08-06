import json
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from new import CareerRecommendationApp
from Databases.questionsDB import Base, UserResponse,save_responses
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Window.size = (350, 600)
# Define the data file where user profiles will be stored
USER_DATA_FILE = "user_profiles.json"
engine = create_engine('sqlite:///user_answers.db')


# Create a dictionary to store user profiles
user_profiles = {}
login_details = {}
# Define the quiz questions and answers

def read_questions_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


questions = read_questions_from_file("Questions.txt")

# questions = [
#     {
#         "question": "Are you detailed oriented?",
#         "answer": True,
#     },
#     {
#         "question": "Are you a team player?",
#         "answer": True,
#     },
#     {
#         "question": "Are you a creative and critical thinker?",
#         "answer": False,
#     },
# ]


class LoginScreen(Screen):
    def do_login(self):
        username = self.ids.email_input.text
        password = self.ids.password_input.text

        if username in user_profiles and user_profiles[username]["password"] == password:
            self.manager.current = "quiz_screen"
        else:
            self.ids.login_error.text = "Invalid username or password"


class SignUpScreen(Screen):
    def do_signup(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        if email not in user_profiles:
            user_profiles[email] = {"password": password}
            self.manager.current = "login_screen"
            self.save_user_data()
        else:
            self.ids.signup_error.text = "Username already exists"

    def save_user_data(self):
        with open(USER_DATA_FILE, "w") as f:
            json.dump(user_profiles, f)


class QuizScreen(Screen):


    pass
class WindowManager(ScreenManager):
    pass




class MyApp(MDApp):
    def build(self):
        self.index = 0
        self.dialog = None
        self.theme_cls.primary_palette = "Pink"

        self.load_user_data()
        self.root = Builder.load_file("app.kv")  # Move the kv file loading here
        return self.root

    def load_user_data(self):
        try:
            with open(USER_DATA_FILE, "r") as f:
                global user_profiles
                user_profiles = json.load(f)
        except FileNotFoundError:
            pass
        
    def show_next_question(self):
        if self.index < len(questions):
            self.show_question(questions[self.index])
            self.index += 1
        else:
            # self.save_responses(self.response)  
            career_app = mmCareerRecommendationApp()
            
    def save_responses(self,response):
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Insert the responses into the database
        for i, response in enumerate(self.responses):
            question = self.questions[i]
            user_response = UserResponse(question=question, response=response)
            session.add(user_response)

        # Commit the changes and close the session
        session.commit()
        session.close()


    def show_question(self, question):
        self.dialog = MDDialog(
            title=question,
            buttons=[
                MDRaisedButton(text="YES", on_release=self.check_answer),
                MDRaisedButton(text="NO", on_release=self.check_answer),
            ],
        )
        self.dialog.open()

        
    def check_answer(self, instance):
        if self.index <= 0 or self.index > len(questions):
        # Invalid index, maybe the user tried to access the answer without showing the question.
            return

        self.dialog.dismiss()
        self.show_next_question()
        
   
    # def show_result(self):
    #     CareerRecommendationApp(MDApp)
    #     correct_answers = sum(question["answer"] for question in questions)
    #     total_questions = len(questions)
    #     result = f"You scored {correct_answers} out of {total_questions} questions correctly."
    #     self.dialog = MDDialog(title="Quiz Result", text=result)
    #     self.dialog.open()


if __name__ == "__main__":
    MyApp().run()
    
