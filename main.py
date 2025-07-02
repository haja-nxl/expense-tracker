import os
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Initialize CSV file with headers if it doesn't exist
if not os.path.exists(EXPENSE_FILE):
    with open(EXPENSE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    """Add a new expense to the tracker."""
    date = input("Enter date (YYYY-MM-DD) [Today]: ") or datetime.now().strftime("%Y-%m-%d")
    category = input("Category (Food, Rent, Entertainment, etc.): ").capitalize()
    amount = float(input("Amount ($): "))
    description = input("Description (Optional): ")

    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!")

def view_expenses():
    """Display all expenses in a readable table."""
    try:
        df = pd.read_csv(EXPENSE_FILE)
        if df.empty:
            print("No expenses recorded yet.")
        else:
            print("\n📝 All Expenses:")
            print(df.to_string(index=False))
    except FileNotFoundError:
        print("No expenses recorded yet.")

def summary_by_category():
    """Show total spending per category."""
    try:
        df = pd.read_csv(EXPENSE_FILE)
        if df.empty:
            print("No expenses to summarize.")
        else:
            summary = df.groupby('Category')['Amount'].sum()
            print("\n📊 Spending by Category:")
            print(summary.to_string())

            # Plotting
            summary.plot(kind='bar', title='Expense Distribution')
            plt.xlabel('Category')
            plt.ylabel('Amount ($)')
            plt.show()
    except FileNotFoundError:
        print("No expenses recorded yet.")

def delete_expense():
    """Remove an expense by index."""
    view_expenses()
    try:
        df = pd.read_csv(EXPENSE_FILE)
        if df.empty:
            print("No expenses to delete.")
            return

        index = int(input("\nEnter the row number to delete: "))
        if 0 <= index < len(df):
            df = df.drop(index).reset_index(drop=True)
            df.to_csv(EXPENSE_FILE, index=False)
            print("🗑️ Expense deleted!")
        else:
            print("Invalid row number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main menu for the expense tracker."""
    while True:
        print("\n💵 Expense Tracker Menu:")
        print("1 ➔ Add Expense")
        print("2 ➔ View Expenses")
        print("3 ➔ Summary by Category")
        print("4 ➔ Delete Expense")
        print("5 ➔ Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()