from .database import get_connection


def add_transaction(date, amount, type, category, description):
    connection = get_connection()
    connection.execute(
        "INSERT INTO transactions (date, amount, type, category, description) "
        "VALUES (?, ?, ?, ?, ?)",
        (date, amount, type, category, description),
    )
    connection.commit()
    connection.close()


def get_transactions():
    connection = get_connection()
    results = connection.execute("SELECT * FROM transactions").fetchall()
    connection.close()
    return results
