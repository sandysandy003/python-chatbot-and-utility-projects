
# Task 5: Student Study Assistant

def explain_topic(topic):
    return (
        f"STUDY TOPIC: {topic}\n\n"
        f"Simple explanation:\n"
        f"{topic} is the subject you are learning. "
        "Break it into smaller ideas and understand each one with examples.\n\n"
        "5 Important Study Points:\n"
        "1. Understand the basic definition.\n"
        "2. Learn the key concepts.\n"
        "3. Study a practical example.\n"
        "4. Review common applications.\n"
        "5. Practise explaining it in your own words.\n\n"
        "3 Practice Questions:\n"
        f"1. What is {topic}?\n"
        f"2. Why is {topic} important?\n"
        f"3. Give one example of {topic}.\n\n"
        "Suggested answers:\n"
        f"1. {topic} is the topic being studied.\n"
        f"2. Its importance depends on its uses and applications.\n"
        f"3. Answers will vary depending on the specific topic."
    )

print("=" * 45)
print("STUDENT STUDY ASSISTANT")
print("Type 'exit' to quit.")
print("=" * 45)

while True:
    topic = input("\nEnter a study topic: ").strip()

    if topic.lower() == "exit":
        print("Goodbye!")
        break

    if not topic:
        print("Please enter a topic.")
        continue

    print("\n" + explain_topic(topic))
