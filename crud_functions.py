import sqlite3
import random

connection = sqlite3.connect('database2.db')
cursor = connection.cursor()


# def initiate_db():
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Products(
#         id INT,
#         title TEXT,
#         description TEXT,
#         price INT
#         );
#     ''')
#     connection.commit()

def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INT PRIMARY KEY,
        username TEXT NOT NULL ,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT DEFAULT 1000
        );
    ''')
    connection.commit()

def add_user(username, email, age):
    total1=cursor.execute("SELECT COUNT (*) FROM Users").fetchone()[0]+1
    cursor.execute("INSERT INTO Users (id, username, email, age) VALUES(?, ?, ?, ?)", (total1, username, email, age))
    connection.commit()

def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE id=?', (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True

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
