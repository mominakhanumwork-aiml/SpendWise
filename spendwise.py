
import json
from pathlib import Path

FILE_NAME = Path(__file__).with_name("expenses.json")


# Load previously saved expenses
def load_expenses():
    if FILE_NAME.exists():
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved expenses. Starting with an empty list.")
    return []


# Save expenses permanently
def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    print("\n--- ADD NEW EXPENSE ---")

    title = input("Enter expense name: ").strip()
    category = input("Enter category: ").strip()

    if not title or not category:
        print("Name and category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount in rupees: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    new_expense = {
        "title": title,
        "category": category,
        "amount": amount
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    print("\nSUCCESS! Expense saved.")
    print("Name:", title)
    print("Category:", category)
    print("Amount: Rs.", amount)


# Display all expenses
def view_expenses(expenses):
    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses have been added yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print("\nExpense", number)
        print("Name:", expense["title"])
        print("Category:", expense["category"])
        print("Amount: Rs.", expense["amount"])

    print("\n==================================")


# Calculate total spending
def view_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n========== TOTAL SPENDING ==========")
    print("Number of expenses:", len(expenses))
    print("Total amount: Rs.", round(total, 2))
    print("====================================")


# Filter expenses by category
def view_category(expenses):
    category = input("\nEnter category to search: ").strip().lower()

    found = False
    category_total = 0

    print("\n--- CATEGORY RESULTS ---")

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                expense["title"],
                "- Rs.",
                expense["amount"]
            )
            category_total += expense["amount"]
            found = True

    if found:
        print("Category total: Rs.", round(category_total, 2))
    else:
        print("No expenses found in this category.")


# Main application
def main():
    expenses = load_expenses()

    while True:
        print("\n========== SPENDWISE ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. Search by Category")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            view_total(expenses)

        elif choice == "4":
            view_category(expenses)

        elif choice == "5":
            print("\nThank you for using SpendWise!")
            print("Your expenses have been saved.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

        if choice in ("1", "2", "3", "4"):
            input("\nPress ENTER to return to the main menu...")


if __name__ == "__main__":
    main()
