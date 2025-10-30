# WAP that generates a Quiz
# Use two files Questions.text and answers.txt
# Program opens Questions.txt and reads a question and displays the question with options on the screen.
# The program then opens ANswers.txt file and display correct answers

# quiz_generator.py


def load_questions(filename):
    """Read and return all questions from file."""
    with open(filename, "r") as f:
        data = f.read().strip()
    # Split questions by blank line
    questions = data.split("\n\n")
    return questions


def load_answers(filename):
    """Read and return all correct answers."""
    with open(filename, "r") as f:
        answers = [line.strip().lower() for line in f.readlines()]
    return answers


def main():
    qfile = "Questions.txt"
    afile = "Answers.txt"

    try:
        questions = load_questions(qfile)
        answers = load_answers(afile)

        print("\n===== QUIZ TIME! =====\n")
        score = 0

        for i, question in enumerate(questions):
            print(question)
            user_ans = input("Your answer (a/b/c/d): ").strip().lower()

            if i < len(answers) and user_ans == answers[i]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! Correct answer: {answers[i]}\n")

        print("===== QUIZ OVER =====")
        print(f"Your Score: {score}/{len(questions)}")

    except FileNotFoundError:
        print(
            "\nOne or both files not found! Make sure 'Questions.txt' and 'Answers.txt' exist."
        )


if __name__ == "__main__":
    main()
