# Import necessary Kivy modules
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Define the Kivy language string with the necessary widget IDs
Builder.load_string('''
<QuizScreen>:
    MDLabel:
        id: question_label
        text: "Default text for the MDLabel"
        halign: 'center'
        valign: 'middle'
''')

# Define the QuizScreen class
class QuizScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.change_label_text()

    def change_label_text(self):
        # Access the MDLabel widget by its ID
        question_label = self.ids.question_label
        question_label.text = "New text for the MDLabel"
