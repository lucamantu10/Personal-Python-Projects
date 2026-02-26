def show_menu():
    print("\n===== EXPENSE TRACKER =====\n")
    print("1) Add expense")
    print("2) List expenses")
    print("3) Show total: ")
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
    with open("data/expenses.txt", "a") as file:
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
        with open("data/expenses.txt", "r") as file:
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
    confirm = input("Are you sure you want to erase ALL data? (Yes/No)").strip().lower()
    if confirm != "Yes":
        print("Canceled!")
        return

    with open("data/expenses.txt", "w") as file:
        pass

print("Expense erased!")



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
        elif choice == 0:
            print("Goodbye!")
            break
        else :
            print("Invalid choice!")

if __name__ == "__main__":
    main()