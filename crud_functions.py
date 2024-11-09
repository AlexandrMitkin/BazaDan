import sqlite3
import random

connection = sqlite3.connect('database2.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INT,
        title TEXT,
        description TEXT,
        price INT
        );
    ''')
    connection.commit()


def set_all_products():
    for i in range(4):
        cursor.execute("INSERT INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)",
                       (i + 1, f'Продукт{i + 1}', f"Описание{i + 1}", 100 * (i + 1)))
    connection.commit()


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    # connection.commit()
    return cursor.fetchall()


if __name__ == "__main__":
    connection.commit()
    connection.close()
