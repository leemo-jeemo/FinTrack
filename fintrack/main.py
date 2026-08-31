from .database import initialize_database
from .transactions import (
    add_transaction,
    get_transactions,
    delete_transaction,
    update_transaction,
    get_transactions_by_category,
)
from datetime import datetime


def validate_date(date):
    try:
        parsed_date = datetime.strptime(date, "%m-%d-%Y")
        return parsed_date.strftime("%m-%d-%Y") == date
    except ValueError:
        return False


def get_required_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        print("Input cannot be empty")


def display_transactions(transactions):
    if not transactions:
        print("No transactions found")
        return

    for transaction in transactions:
        print("Transaction ID:", transaction[0])
        print("Transaction Date:", transaction[1])
        print("Transaction Cost:", transaction[2])
        print("Transaction Type:", transaction[3])
        print("Transaction Category:", transaction[4])
        print("Transaction Description:", transaction[5])
        print("-----------------")


def add_transaction_menu():
    while True:
        date = input("Transaction Date: ")
        if validate_date(date):
            while True:
                try:
                    amount = float(input("Transaction Cost: "))

                    if amount <= 0:
                        print("Amount must be greater than 0")
                        continue

                    break
                except ValueError:
                    print("Invalid Amount")
            type = get_required_input("Transaction Type: ")
            category = get_required_input("Transaction Category: ")
            description = get_required_input("Transaction Description: ")
            add_transaction(date, amount, type, category, description)
            print("Transaction Added")

            return
        else:
            print("Invalid Date - MM-DD-YYYY")


def view_transactions():
    while True:
        choice = input("View Menu\n1. View All\n2. View by Category\n3. Back\nChoice: ")
        if choice == "1":
            transactions = get_transactions()
            display_transactions(transactions)
        elif choice == "2":
            category = get_required_input("Category: ")
            transactions = get_transactions_by_category(category)
            display_transactions(transactions)
        elif choice == "3":
            return


def update_transaction_menu():
    while True:
        try:
            transaction_id = int(input("Transaction ID to Update: "))
            break
        except ValueError:
            print("Invalid transaction ID")
    while True:
        date = input("New Transaction Date: ")

        if validate_date(date):
            break
        else:
            print("Invalid Date - MM-DD-YYYY")
    while True:
        try:
            amount = float(input("New Transaction Cost: "))

            if amount <= 0:
                print("Amount must be greater than 0")
                continue
            break
        except ValueError:
            print("Invalid Amount")

    type = get_required_input("New Transaction Type: ")
    category = get_required_input("New Transaction Category: ")
    description = get_required_input("New Transaction Description: ")

    result = update_transaction(
        transaction_id, date, amount, type, category, description
    )

    if result == 1:
        print("Transaction Updated")
        return
    else:
        print("Transaction Not Found")


def delete_transaction_menu():
    while True:
        try:
            transaction_id = int(input("Transaction ID to Delete: "))
        except ValueError:
            print("Invalid transaction ID")
            continue

        result = delete_transaction(transaction_id)

        if result == 1:
            print("Transaction Deleted")
            return
        else:
            print("Transaction Not Found")


def main():
    print("Database initializing...")
    initialize_database()
    while True:
        choice = input(
            "1. Add\n2. View\n3. Update\n4. Delete\n5. Exit\nChoose: "
        ).strip()
        if not choice:
            print("Please enter a menu option.")
            continue
        if choice == "1":
            add_transaction_menu()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            update_transaction_menu()
        elif choice == "4":
            delete_transaction_menu()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
