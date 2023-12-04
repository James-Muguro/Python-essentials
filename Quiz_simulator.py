## Quiz Simulator

def run_quiz():
    print("Welcome to the Python Quiz!")

    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "How many continents are there?", "answer": "7"},
        {"question": "What is 5 + 7?", "answer": "12"}
    ]

    score = 0

    for i, question in enumerate(questions, start=1):
        user_answer = input(f"Question {i}: {question['question']}? ").strip()

        if user_answer.lower() == question['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")

    print(f"Quiz complete! You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()