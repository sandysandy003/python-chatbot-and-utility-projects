
# Task 2: Chatbot with Conversation History
# Local demo: no API key or internet connection required.

history = []

print("=" * 45)
print("CHATBOT WITH CONVERSATION HISTORY")
print("Type 'exit' to quit.")
print("=" * 45)

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question:
        print("Please enter a question.")
        continue

    history.append({"role": "user", "content": question})

    if len(history) == 1:
        answer = "Hello! I've started remembering our conversation."
    else:
        previous_question = history[-3]["content"]
        answer = (
            f"I remember your earlier question: '{previous_question}'. "
            f"Your latest message is: '{question}'."
        ) if len(history) >= 3 else (
            f"I remember you said: '{history[0]['content']}'."
        )

    history.append({"role": "assistant", "content": answer})
    print("\nBot:", answer)
