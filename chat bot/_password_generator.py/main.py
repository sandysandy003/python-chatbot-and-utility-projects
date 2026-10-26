
# Task 12: Password Generator

import secrets
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password includes different character types.
    required = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    remaining = [
        secrets.choice(characters)
        for _ in range(length - len(required))
    ]

    password_chars = required + remaining
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

print("=" * 40)
print("SECURE PASSWORD GENERATOR")
print("=" * 40)

while True:
    choice = input(
        "\nEnter password length (8-128), or type EXIT: "
    ).strip()

    if choice.lower() == "exit":
        print("Goodbye!")
        break

    try:
        length = int(choice)

        if not 8 <= length <= 128:
            print("Choose a length between 8 and 128.")
            continue

        password = generate_password(length)
        print("\nGenerated password:")
        print(password)
        print("\nStore it securely and do not share it.")

    except ValueError as error:
        print(f"Invalid input: {error}")
