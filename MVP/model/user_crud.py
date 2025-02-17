import sqlite3
from MVP.cogs.find_DataBase import FindDB


class UserCRUD:
    def __init__(self, db_path = FindDB().find_database_path()):
        self.db_path = db_path

    def create_user(self, username, password, role):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users (username, password, role, ban) VALUES (?, ?, ?, ?)",
                       (username, password, role, 0))

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

    def ban_user(self, username):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE users SET ban = 1 WHERE username = ?", (username,))

        connection.commit()
        connection.close()