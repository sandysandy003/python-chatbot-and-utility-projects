
# Task 4: Prompt Engineering Demonstration

def generate_weak_response():
    return "AI is technology that helps computers perform tasks."

def generate_strong_response():
    return (
        "Artificial Intelligence (AI) is technology that enables computers "
        "to perform tasks that usually require human intelligence.\n"
        "Example: A navigation app uses AI to suggest the fastest route.\n"
        "Other examples include voice assistants, translation apps, and "
        "recommendation systems."
    )

print("=" * 45)
print("PROMPT ENGINEERING CHATBOT")
print("=" * 45)

weak_prompt = "Explain AI"
strong_prompt = (
    "Explain AI to a beginner in simple English "
    "with one real-world example."
)

print("\nWEAK PROMPT:")
print(weak_prompt)
print("\nResponse:")
print(generate_weak_response())

print("\n" + "-" * 45)

print("\nSTRONG PROMPT:")
print(strong_prompt)
print("\nResponse:")
print(generate_strong_response())

print("\n" + "=" * 45)
print("COMPARISON")
print("The strong prompt specifies the audience, language, and example.")
print("This is a local demonstration; no AI API is called.")
