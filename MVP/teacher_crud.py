from model.teacher_crud import TeacherCRUD


class TeacherTEST:
    def __init__(self, TeacherCRUD = TeacherCRUD()):
        self.TeacherCRUD = TeacherCRUD

    def test(self):

        self.TeacherCRUD.create_teacher('Anton', 124, 2)
        print(self.TeacherCRUD.get_teacher(1))
        self.TeacherCRUD.update_teacher('Maksim', 13333, 1)
        print(self.TeacherCRUD.get_teacher(1))
        self.TeacherCRUD.delete_teacher(1)
        try:
            print(self.TeacherCRUD.get_teacher(1))
        except:
            pass

Test = TeacherTEST()
Test.test()