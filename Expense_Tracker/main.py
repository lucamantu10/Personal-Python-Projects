def show_menu():
    print("\n===== EXPENSE TRACKER =====\n")
    print("1) Add expense")
    print("2) List expenses")
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
    with open("expenses.txt", "a") as file:
        line = f"{category} {amount} {description}\n"
        file.write(line)


def add_expense():
    amount = get_amount()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    save_expense(amount, category, description)
    print("Expense saved successfully!")


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
            print("List expenses!")
        elif choice == 0:
            print("Goodbye!")
            break
        else :
            print("Invalid choice!")

if __name__ == "__main__":
    main()