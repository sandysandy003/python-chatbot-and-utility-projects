
# Task 11: Python Quiz Generator

questions = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. create"],
        "answer": "B",
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. str", "B. int", "C. bool", "D. list"],
        "answer": "C",
    },
    {
        "question": "Which symbol starts a Python comment?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C",
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A. append()", "B. add_end()", "C. insert_end()", "D. push()"],
        "answer": "A",
    },
    {
        "question": "Which function displays output?",
        "options": ["A. show()", "B. print()", "C. output()", "D. display()"],
        "answer": "B",
    },
]

score = 0

print("=" * 40)
print("PYTHON QUIZ GENERATOR")
print("=" * 40)
print("Enter A, B, C, or D.\n")

for number, item in enumerate(questions, start=1):
    print(f"{number}. {item['question']}")

    for option in item["options"]:
        print("  " + option)

    while True:
        answer = input("Your answer: ").strip().upper()
        if answer in ("A", "B", "C", "D"):
            break
        print("Please enter A, B, C, or D.")

    if answer == item["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Not quite. Correct answer: {item['answer']}\n")

print("=" * 40)
print(f"Your score: {score}/{len(questions)}")
print(f"Percentage: {score / len(questions) * 100:.0f}%")
print("=" * 40)
