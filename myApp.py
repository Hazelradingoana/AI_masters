import json
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (350, 600)
# Define the data file where user profiles will be stored
USER_DATA_FILE = "user_profiles.json"

# Create a dictionary to store user profiles
user_profiles = {}


class LoginScreen(Screen):
    def do_login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        if username in user_profiles and user_profiles[username]["password"] == password:
            self.manager.current = "quiz_screen"
        else:
            self.ids.login_error.text = "Invalid username or password"


class SignUpScreen(Screen):
    def do_signup(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        if username not in user_profiles:
            user_profiles[username] = {"password": password}
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


if __name__ == "__main__":
    MyApp().run()
