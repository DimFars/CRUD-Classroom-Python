from teachers import Teachers
from students import Students

class Lesson:
    def __init__(self, lesson_name="", lesson_id=-1):
        self.lesson_name = lesson_name
        self.lesson_id = lesson_id
        self.teacher_ids = []
        self.student_ids = []
    
    def from_dict(self, lesson_dict):
        self.lesson_name = lesson_dict["lesson_name"]
        self.lesson_id = lesson_dict["lesson_id"]
        self.student_ids = lesson_dict["student_ids"]
        self.teacher_id = lesson_dict["teacher_id"]
    
    def to_dict(self):
        lesson_dict = {"lesson_name": self.lesson_name,
                       "lesson_id": self.lesson_id,
                       "student_ids": self.student_ids,
                       "teacher_id": self.teacher_ids}
        return lesson_dict
    
    def print_lesson_details(self, teachers, students):
        st = f"LESSON: {self.lesson_name} \n========\nTEACHERS: "
        for teacher_id in self.teacher_ids:
            teacher = teachers.read_teacher(teacher_id)
            st += f"\n{teacher}"
        st += f"\nSTUDENTS: "
        for student_id in self.student_ids:
            student = students.search_student_by_id(student_id)
            st += f"\n{student.first_name} {student.last_name}"
        print(st)

    
