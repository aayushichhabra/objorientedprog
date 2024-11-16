import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

class Expense:
    """
    Represents an individual expense.
    """
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.datetime.now()

    def __repr__(self):
        return f"💸 {self.amount} INR | {self.category.capitalize()} | {self.description} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

class SmartExpenseApp:
    """
    Main application logic for SmartExpense.
    Manages expenses, budgets, and recurring payments.
    """
    def __init__(self):
        self.expenses = []  # List of all expenses
        self.budget = defaultdict(float)  # Budget per category
        self.recurring_expenses = []  # List of recurring expenses
        self.valid_categories = ['food', 'transport', 'entertainment', 'utilities', 'rent', 'subscription', 'others']

    def display_categories(self):
        """
        Display numbered categories for user selection.
        """
        print("\n📂 Categories:")
        for i, category in enumerate(self.valid_categories, start=1):
            print(f"  {i}. {category.capitalize()}")

    def get_category_by_number(self):
        """
        Let the user choose a category by number.
        """
        while True:
            self.display_categories()
            try:
                choice = int(input("👉 Choose a category by number: "))
                if 1 <= choice <= len(self.valid_categories):
                    return self.valid_categories[choice - 1]
                else:
                    print("🚫 Invalid choice. Please select a valid category number.")
            except ValueError:
                print("🚫 Invalid input. Please enter a number.")

    def get_positive_float(self, prompt):
        """
        Utility method to ensure the user inputs a positive float.
        """
        while True:
            try:
                value = float(input(prompt))
                if value > 0:
                    return value
                else:
                    print("🚫 Please enter a positive number.")
            except ValueError:
                print("🚫 Invalid input. Please enter a valid number.")

    def add_expense(self):
        """
        Add a new expense.
        """
        print("\n✨ --- Add Expense --- ✨")
        amount = self.get_positive_float("Enter the amount spent (in INR): ")
        category = self.get_category_by_number()
        description = input("Enter a description for the expense: ").strip()

        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print(f"✅ Expense added: {expense}")
        self.check_budget(category)

    def set_budget(self):
        """
        Set a budget for a specific category.
        """
        print("\n🎯 --- Set Budget --- 🎯")
        category = self.get_category_by_number()
        budget_amount = self.get_positive_float(f"Enter your monthly budget for {category.capitalize()} (in INR): ")
        self.budget[category] = budget_amount
        print(f"✅ Budget set for {category.capitalize()}: {budget_amount} INR")

    def view_budget(self):
        """
        View budgets for all categories, including remaining amounts.
        """
        print("\n🎯 --- View Budgets --- 🎯")
        if not self.budget:
            print("🚫 No budgets set yet.")
            return

        for category, budget_amount in self.budget.items():
            total_spent = sum(exp.amount for exp in self.expenses if exp.category == category)
            remaining_budget = budget_amount - total_spent
            print(f"📂 {category.capitalize()}: Budget = {budget_amount:.2f} INR, Spent = {total_spent:.2f} INR, Remaining = {remaining_budget:.2f} INR")

    def check_budget(self, category):
        """
        Check if the user has exceeded their budget for the given category.
        """
        total_spent = sum(exp.amount for exp in self.expenses if exp.category == category)
        remaining_budget = self.budget.get(category, 0) - total_spent
        if remaining_budget < 0:
            print(f"⚠️ Warning: You have exceeded your budget for {category.capitalize()} by {-remaining_budget:.2f} INR!")
        else:
            print(f"✅ Remaining budget for {category.capitalize()}: {remaining_budget:.2f} INR")

    def view_expenses(self):
        """
        Display all recorded expenses.
        """
        print("\n📜 --- View Expenses --- 📜")
        if not self.expenses:
            print("🚫 No expenses recorded yet.")
        else:
            print("\n".join([str(expense) for expense in self.expenses]))

    def set_recurring_expenses(self):
        """
        Add a recurring expense (e.g., rent, subscription).
        """
        print("\n🔄 --- Set Recurring Expense --- 🔄")
        amount = self.get_positive_float("Enter recurring expense amount (in INR): ")
        category = self.get_category_by_number()
        description = input("Enter a description for the recurring expense: ").strip()
        frequency = input("Enter frequency (weekly, monthly, etc.): ").lower()

        recurring_expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'frequency': frequency,
            'next_due': datetime.datetime.now()
        }
        self.recurring_expenses.append(recurring_expense)
        print(f"✅ Recurring expense added: {recurring_expense}")

    def view_recurring_expenses(self):
        """
        Display all recurring expenses.
        """
        print("\n🔁 --- Recurring Expenses --- 🔁")
        if not self.recurring_expenses:
            print("🚫 No recurring expenses set.")
        else:
            for expense in self.recurring_expenses:
                print(expense)

    def show_expense_report(self):
        """
        Display a report of all expenses grouped by category and generate a pie chart.
        """
        print("\n📊 --- Expense Report --- 📊")
        if not self.expenses:
            print("🚫 No expenses recorded yet.")
            return

        # Group expenses by category
        category_totals = defaultdict(float)
        for expense in self.expenses:
            category_totals[expense.category] += expense.amount

        print("\n🗂️ Category-wise Expense Summary:")
        for category, total in category_totals.items():
            print(f"  📂 {category.capitalize()}: {total:.2f} INR")

        # Generate a pie chart of the expenses by category
        self.plot_expenses_pie_chart(category_totals)

    def plot_expenses_pie_chart(self, category_totals):
        """
        Create and display a pie chart for expenses grouped by category.
        """
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        plt.figure(figsize=(7, 7))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title("Expense Breakdown by Category (INR)")
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def process_recurring_expenses(self):
        """
        Add recurring expenses to the main expenses list if their due date is today or earlier.
        """
        print("\n🔄 --- Processing Recurring Expenses --- 🔄")
        current_date = datetime.datetime.now()
        for recurring in self.recurring_expenses:
            while recurring['next_due'] <= current_date:
                # Create a new Expense object
                expense = Expense(
                    amount=recurring['amount'],
                    category=recurring['category'],
                    description=f"Recurring: {recurring['description']}",
                    date=recurring['next_due']
                )
                self.expenses.append(expense)

                # Update next_due based on frequency
                if recurring['frequency'] == 'monthly':
                    recurring['next_due'] += datetime.timedelta(days=30)
                elif recurring['frequency'] == 'weekly':
                    recurring['next_due'] += datetime.timedelta(weeks=1)
                else:
                    print(f"⚠️ Unsupported frequency: {recurring['frequency']}. Skipping.")
                    break
                print(f"✅ Processed recurring expense: {expense}")
        print("🔄 Recurring expenses processed.")

    def display_main_menu(self):
        """
        Display the main menu and handle user selection.
        """
        while True:
            print("\n🌟 --- SmartExpense App --- 🌟")
            print("1️⃣  Add Expense")
            print("2️⃣  Set Budget")
            print("3️⃣  View Budgets")
            print("4️⃣  View Expenses")
            print("5️⃣  Set Recurring Expenses")
            print("6️⃣  View Recurring Expenses")
            print("7️⃣  Process Recurring Expenses")
            print("8️⃣  Show Expense Report")
            print("9️⃣  Exit")
            print("💡 Tip: Set your budgets before adding expenses!")

            choice = input("👉 Choose an option (1-9): ").strip()
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.set_budget()
            elif choice == '3':
                self.view_budget()
            elif choice == '4':
                self.view_expenses()
            elif choice == '5':
                self.set_recurring_expenses()
            elif choice == '6':
                self.view_recurring_expenses()
            elif choice == '7':
                self.process_recurring_expenses()
            elif choice == '8':
                self.show_expense_report()
            elif choice == '9':
                print("👋 Exiting SmartExpense... Goodbye!")
                break
            else:
                print("🚫 Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    app = SmartExpenseApp()
    app.display_main_menu()
