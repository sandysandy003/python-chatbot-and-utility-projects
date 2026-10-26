
# Task 9: Professional Email Generator
# Local template-based demo — no API requests required.

def generate_email(recipient, purpose, reason, subject):
    email = f"""Subject: {subject}

Dear {recipient},

I hope you are doing well.

I am writing to {purpose}. {reason}

Thank you for your time and consideration. I look forward to hearing from you.

Best regards,
[Your Name]"""
    return email

print("=" * 45)
print("PROFESSIONAL EMAIL GENERATOR")
print("Type 'exit' at any prompt to quit.")
print("=" * 45)

while True:
    recipient = input("\nRecipient (e.g., Professor, Manager): ").strip()
    if recipient.lower() == "exit":
        break

    subject = input("Email subject: ").strip()
    if subject.lower() == "exit":
        break

    purpose = input("Purpose (e.g., request an assignment extension): ").strip()
    if purpose.lower() == "exit":
        break

    reason = input("Reason or extra details: ").strip()
    if reason.lower() == "exit":
        break

    if not all([recipient, subject, purpose, reason]):
        print("Please fill in every field.")
        continue

    print("\n" + "=" * 45)
    print(generate_email(recipient, purpose, reason, subject))
    print("=" * 45)
