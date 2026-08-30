from .database import initialize_database
from .transactions import add_transaction, get_transactions
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
        date = input("Transaction Date:")
        if validate_date(date):
            amount = float(input("Transaction Cost:"))
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


if __name__ == "__main__":
    main()
