from .database import initialize_database
from .transactions import (
    add_transaction,
    get_transactions,
    delete_transaction,
    update_transaction,
)
from datetime import datetime


def validate_date(date):
    try:
        parsed_date = datetime.strptime(date, "%m-%d-%Y")
        return parsed_date.strftime("%m-%d-%Y") == date
    except ValueError:
        return False


def main():
    print("Database initializing...")
    initialize_database()
    while True:
        choice = input("1. Add\n2. View\n3. Update\n4. Delete\n5. Exit\nChoose: ")
        if choice == "1":
            while True:
                date = input("Transaction Date:")
                if validate_date(date):
                    while True:
                        try:
                            amount = float(input("Transaction Cost:"))
                            break
                        except ValueError:
                            print("Invalid Amount")
                    type = input("Transaction Type:")
                    category = input("Transaction Category:")
                    description = input("Transaction Description:")
                    add_transaction(date, amount, type, category, description)
                    print("Transaction Added")
                    transactions = get_transactions()
                    for transaction in transactions:
                        print(transaction)
                    break
                else:
                    print("Invalid Date - MM-DD-YYYY")
        elif choice == "2":
            transactions = get_transactions()
            for transaction in transactions:
                print("Transaction ID:", transaction[0])
                print("Transaction Date:", transaction[1])
                print("Transaction Cost:", transaction[2])
                print("Transaction Type:", transaction[3])
                print("Transaction Category:", transaction[4])
                print("Transaction Description:", transaction[5])
                print("-----------------")
        elif choice == "3":
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
                        amount = float(input("New Transaction Cost:"))
                        break
                    except ValueError:
                        print("Invalid Amount")

                type = input("New Transaction Type: ")
                category = input("New Transaction Category: ")
                description = input("New Transaction Description: ")

                result = update_transaction(
                    transaction_id, date, amount, type, category, description
                )

                if result == 1:
                    print("Transaction Updated")
                    break
                else:
                    print("Transaction Not Found")
        elif choice == "4":
            while True:
                try:
                    transaction_id = int(input("Transaction ID to Delete: "))
                except ValueError:
                    print("Invalid transaction ID")
                    continue

                result = delete_transaction(transaction_id)

                if result == 1:
                    print("Transaction Deleted")
                    break
                else:
                    print("Transaction Not Found")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
