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


def delete_transaction(transaction_id):
    connection = get_connection()
    cursor = connection.execute(
        "DELETE FROM transactions WHERE id = ?",
        (transaction_id,),
    )
    connection.commit()
    connection.close()
    return cursor.rowcount


def update_transaction(transaction_id, date, amount, type, category, description):
    connection = get_connection()
    cursor = connection.execute(
        "UPDATE transactions SET date = ?, amount = ?, type = ?, category = ?, description = ? WHERE id = ?",
        (date, amount, type, category, description, transaction_id),
    )
    connection.commit()
    connection.close()

    return cursor.rowcount


def get_transactions_by_category(category):
    connection = get_connection()
    results = connection.execute(
        "SELECT * FROM transactions WHERE category = ?", (category,)
    ).fetchall()
    connection.close()
    return results
