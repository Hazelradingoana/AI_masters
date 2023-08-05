def read_questions(file_path):
    with open(file_path, 'r') as file:
        questions = file.readlines()
    return [question.strip() for question in questions]

def ask_questions(questions):
    user_responses = []
    for question in questions:
        while True:
            response = input(f"{question} (yes/no): ").strip().lower()
            if response in ['yes', 'no']:
                user_responses.append(response)
                break
            print("Please enter 'yes' or 'no'.")

    return user_responses

def main():
    questions_file = "Questions.txt"
    questions = read_questions(questions_file)
    user_responses = ask_questions(questions)

    # Process user_responses or provide recommendations based on their answers
    # ...

if __name__ == "__main__":
    main()
