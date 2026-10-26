
# Task 14: Expense Tracker

import csv
from pathlib import Path
from datetime import date

DATA_FILE = Path(__file__).with_name("expenses.csv")
FIELDS = ["date", "category", "description", "amount"]


def load_expenses():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_expense(expense):
    file_exists = DATA_FILE.exists()

    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_exists or DATA_FILE.stat().st_size == 0:
            writer.writeheader()

        writer.writerow(expense)


def add_expense():
    category = input("Category (food, travel, bills, etc.): ").strip()
    description = input("Description: ").strip()
    amount_text = input("Amount: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    try:
        amount = float(amount_text)
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "date": date.today().isoformat(),
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}",
    }

    save_expense(expense)
    print("Expense saved successfully.")


def show_expenses():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\nYOUR EXPENSES")
    total = 0.0

    for item in expenses:
        amount = float(item["amount"])
        total += amount
        print(
            f"{item['date']} | {item['category']} | "
            f"{item['description']} | {amount:.2f}"
        )

    print("-" * 45)
    print(f"Total expenses: {total:.2f}")


def category_summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to summarize.")
        return

    totals = {}

    for item in expenses:
        category = item["category"]
        totals[category] = totals.get(category, 0.0) + float(item["amount"])

    print("\nCATEGORY SUMMARY")
    for category, total in sorted(totals.items()):
        print(f"{category}: {total:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses and total")
        print("3. Summary by category")
        print("4. Exit")

        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("Your expenses are saved. Goodbye!")
            break
        else:
            print("Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
