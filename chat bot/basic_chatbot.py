
print("=" * 40)
print("BASIC PYTHON CHATBOT")
print("Type 'exit' to quit.")
print("=" * 40)

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question:
        print("Please enter a question.")
    else:
        print("Bot: You asked:", question)
        print("Bot: This is a basic demo chatbot.")
