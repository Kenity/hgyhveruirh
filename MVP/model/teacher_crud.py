import sqlite3
from MVP.cogs.find_DataBase import FindDB


class TeacherCRUD:
    def __init__(self, db_path = FindDB().find_database_path()):
        self.db_path = db_path

    def create_teacher(self, name, phone, user_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO teachers (name, phone, user_id) VALUES (?, ?, ?)",
                       (name, phone, user_id))
        connection.commit()
        connection.close()

    def get_teacher(self, teacher_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        teacher = cursor.execute("SELECT * FROM teachers WHERE teacher_id = ?", (teacher_id,)).fetchall()

        connection.close()
        return teacher

    def update_teacher(self, name, phone, teacher_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE teachers SET name = ?, phone = ? WHERE teacher_id = ?",
                       (name, phone, teacher_id))
        connection.commit()
        connection.close()

    def delete_teacher(self, teacher_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("DELETE FROM teachers WHERE teacher_id = ?", (teacher_id,))

        connection.commit()
        connection.close()
