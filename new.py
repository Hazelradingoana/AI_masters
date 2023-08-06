import json
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
    

# Career mapping data
career_mapping_data = {
    "Software Developer": [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    "Data Scientist": [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    "Web Developer": [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    "Machine Learning Engineer": [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    "Cybersecurity Analyst": [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    "Database Administrator": [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    "UI/UX Designer": [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1]
}

# Question weights data
question_weights_data = [3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

class CareerRecommendationApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(
            '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: "Career Recommendation App"
        md_bg_color: 0.2, 0.2, 0.2, 1
        specific_text_color: 1, 1, 1, 1

    ScrollView:
        MDList:
            id: recommendations_list

    MDRaisedButton:
        text: "Get Recommendations"
        on_release: app.show_recommendations()
            '''
        )

    def show_recommendations(self):
        questions = self.read_questions_from_file("Questions.txt")

        user_responses = self.get_user_responses(questions)

        career_mapping = career_mapping_data
        question_weights = question_weights_data

        scores = self.calculate_scores(user_responses, career_mapping, question_weights)
        recommendations = self.get_career_recommendations(scores)

        recommendations_list = self.root.ids.recommendations_list
        recommendations_list.clear_widgets()

        for i, (career, percentage) in enumerate(recommendations, 1):
            item_text = f"{i}. {career} - {percentage}"
            recommendations_list.add_widget(MDLabel(text=item_text, halign="center"))

    def read_questions_from_file(self, filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    def get_user_responses(self, questions):
        responses = []
        for question in questions:
            response = input(f"{question} (yes/no): ").lower()
            while response not in ["yes", "no"]:
                response = input("Please enter 'yes' or 'no': ").lower()
            responses.append(1 if response == "yes" else 0)
        return responses

    def calculate_scores(self, user_responses, career_mapping, question_weights):
        total_weight = sum(question_weights)
        scores = {}
        for career, career_responses in career_mapping.items():
            score = sum(r * w for r, w in zip(user_responses, career_responses))
            percentage = (score / total_weight) * 100
            scores[career] = (score, percentage)
        return scores

    def get_career_recommendations(self, scores):
        sorted_scores = sorted(scores.items(), key=lambda x: x[1][0], reverse=True)
        return [(career, f"{score:.2f}%") for career, (score, percentage) in sorted_scores]


if __name__ == "__main__":
    CareerRecommendationApp().run()
