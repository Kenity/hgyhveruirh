import sqlite3
from MVP.cogs.find_DataBase import FindDB


class StudentCRUD:
    def __init__(self, db_path = FindDB().find_database_path()):
        self.db_path = db_path

    def create_student(self, name, age, phone, user_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO students (name, age, phone, user_id) VALUES (?, ?, ?, ?)",
                       (name, age, phone, user_id))
        connection.commit()
        connection.close()

    def get_students(self, student_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        student = cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,)).fetchall()

        connection.close()
        return student

    def get_all_students(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        students = cursor.execute("SELECT * FROM students").fetchall()

        connection.close()
        return students

    def update_students(self, name, age, phone, student_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE students SET name = ?, age = ?, phone = ? WHERE student_id = ?",
                       (name, age, phone, student_id))
        connection.commit()
        connection.close()

    def delete_students(self, student_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))

        connection.commit()
        connection.close()

