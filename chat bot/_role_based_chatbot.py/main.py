
# Task 3: Role-Based Chatbot — Python Instructor

def get_answer(question):
    q = question.lower()

    if "variable" in q:
        return "A variable stores a value. Example: age = 20"
    elif "loop" in q or "for loop" in q:
        return "A loop repeats code. Example: for i in range(3): print(i)"
    elif "function" in q:
        return "A function is reusable code. Example: def greet(): print('Hello')"
    elif "list" in q:
        return "A list stores multiple values. Example: fruits = ['apple', 'mango']"
    elif "if" in q or "condition" in q:
        return "An if statement runs code when a condition is true. Example: if age >= 18: print('Adult')"
    else:
        return "I'm your Python instructor. Ask me about variables, loops, functions, lists, or conditions."

print("=" * 45)
print("PYTHON INSTRUCTOR CHATBOT")
print("Type 'exit' to quit.")
print("=" * 45)

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if question:
        print("\nPython Tutor:", get_answer(question))
    else:
        print("Please enter a question.")
