from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.add_widget(Button(text='Go to Second Screen'))
    pass