import sqlite3
from MVP.model.config import settings


class UserCRUD:
    def __init__(self, db_path = settings['DB_PATH']):
        self.db_path = db_path

    def create_user(self, username, password, role):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                       (username, password, role))

        connection.commit()
        connection.close()

    def get_user(self, username):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        user = cursor.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()

        connection.close()
        return user

    def get_all_user(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        users = cursor.execute("SELECT * FROM users").fetchall()

        connection.close()
        return users
    def update_user(self, username, password, role):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE users SET password = ?, role = ? WHERE username = ?",
                       (password, role, username))
        connection.commit()
        connection.close()

    def delete_user(self, username):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("DELETE FROM users WHERE username = ?", (username))
