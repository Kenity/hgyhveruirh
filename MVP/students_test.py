from model.student_crud import StudentCRUD


class StudentsTest:
    def __init__(self, StudentCRUD = StudentCRUD()):
        self.StudentCRUD = StudentCRUD

    def test(self):

        self.StudentCRUD.create_student("Maksim", 15, 555, 2)
        print(self.StudentCRUD.get_students(2))
        self.StudentCRUD.update_students('Anton', 12, 333, 2)
        print(self.StudentCRUD.get_all_students())
        self.StudentCRUD.delete_students(2)
        print(self.StudentCRUD.get_all_students())

Test = StudentsTest()
Test.test()