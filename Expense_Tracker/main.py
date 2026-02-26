EXPENSES_FILE = "data/expenses.txt"
SUMMARY_FILE = "data/monthly_summary.csv"

def show_menu():
    print("\n===== EXPENSE TRACKER =====\n")
    print("1) Add expense")
    print("2) List expenses")
    print("3) Show total spent this month")
    print("4) Reset expenses")
    print("5) Close month")
    print("0) Exit")

def get_amount():
    while True:
        value = input("Enter the amount payed: ").strip()

        try:
            amount = float(value)
            if amount < 0:
                print("The amount must be positive!")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number!")



def save_expense(amount, category, description):
    with open(EXPENSES_FILE, "a") as file:
        line = f" {amount} {category} {description}\n"
        file.write(line)


def add_expense():
    amount = get_amount()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    save_expense(amount, category, description)
    print("Expense saved successfully!")

def load_expenses():
    expenses = []

    try:
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(" ")

                if len(parts) != 3:
                    print(f"Skipping invalid line: {line}")
                    continue

                amount_str, category, description = parts

                try:
                    amount = float(amount_str)
                except ValueError:
                    print(f"Skipping invalid amount: {amount_str}")
                    continue

                expenses.append([amount, category, description])
    except FileNotFoundError:
        return[]

    return expenses


def list_expenses():
    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses saved!")
        return

    print("\n---- Your Expenses ----")
    for amount, category, description in expenses:
        print(f"{amount:.2f} | {category:<10} | {description}")

def show_total():
    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses saved!")
        return

    total = 0

    for amount, category, description in expenses:
        total += amount
    print(f"Total amount spent: {total:.2f}")

def reset_expenses():
    confirm = input("Erase ALL current expenses? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Cancelled.")
        return

    with open(EXPENSES_FILE, "w") as file:
        pass

    print("Current expenses cleared.")


def totals_by_category(expenses):
    totals = {}

    for amount, category, description in expenses:
        if category not in totals:
            totals[category] = 0.0
            totals[category] += amount
    return totals


def close_month():
    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses saved!")
        return

    month = input("Enter month (MM-YYYY): ").strip()

    total = 0.0
    for amount, category, description in expenses:
        total += amount

    cat_totals = totals_by_category(expenses)

    # scriem în SUMMARY_FILE (nu în expenses)
    with open(SUMMARY_FILE, "a") as file:
        for category, cat_total in cat_totals.items():
            file.write(f"{month},{category},{cat_total:.2f}\n")

        file.write(f"{month},__TOTAL__,{total:.2f}\n")

    print("Month archived to monthly_summary.csv")

    with open(EXPENSES_FILE, "w") as file:
        pass

    print("Current expenses cleared for new month.")


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice!")
            continue
        if choice == 1:
            add_expense()
        elif choice == 2:
            list_expenses()
        elif choice == 3:
            show_total()
        elif choice == 4:
            reset_expenses()
        elif choice == 5:
            close_month()
        elif choice == 0:
            print("Goodbye!")
            break
        else :
            print("Invalid choice!")

if __name__ == "__main__":
    main()