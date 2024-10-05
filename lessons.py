import os
import json
from lesson import Lesson

def filepath(filename):
    filepath = os.path.dirname(__file__) + "\\" + filename
    return filepath

class Lessons:
    def __init__(self):
        try:
            with open(filepath("Data_Project_CRUD_Lessons.json")) as f:
                lessons_list = json.load(f)
            self.lessons = []
            for lesson_dict in lessons_list:
                l = Lesson()
                l.from_dict(lesson_dict)
                self.lessons += [l]
        except FileNotFoundError:
            self.lessons = []
        
    def save_lessons_data(self):
        list_to_write = []
        for lesson in self.lessons:
            list_to_write += [lesson.to_dict()]
        
        with open(filepath("Data_Project_CRUD_Lessons.json"), "w") as f:
            json.dump(list_to_write, f)
        
    def next_id(self):
        if not self.lessons:
            return 1001
        else:
            ids = []
            for l in self.lessons:
                ids.append(l.lesson_id)
            return max(ids) + 1

    def create_lesson(self, lesson_name):
        for lesson in self.lessons:
            if lesson.lesson_name == lesson_name:
                print("Error. Lesson already exists! ")
                return None

        l = Lesson(lesson_name, self.next_id())
        self.lessons.append(l)
        return l

    def read_lesson(self, lesson_id):
        for lesson in self.lessons:
            if lesson_id==lesson.lesson_id:
                return lesson
        else:
            return None
    
    def update_lesson(self, lesson_id, teachers, students):
        for lesson in self.lessons:
            if lesson_id == lesson.lesson_id:
                lesson.print_lesson_details(teachers, students)
                choice = int(input("Update 1-name, 2-teachers, 3-students: "))
                if choice == 1:
                    lesson.lesson_name = input("Give new name: ")
                elif choice == 2:
                    upd_teacher_choice = int(input("Updating lesson teachers: 1-add, 2-remove: "))
                    if upd_teacher_choice == 1:
                        print("Teachers(not in lesson): ")
                        for teacher in teachers.teachers:
                            if teacher.teacher_id not in lesson.teacher_ids:
                                print(f"{teacher.teacher_id}-{teacher.first_name} {teacher.surname}")
                        upd_teacher_id = int(input("Pick the (id) to add: "))
                        lesson.teacher_ids.append(upd_teacher_id)
                    elif upd_teacher_choice == 2:
                        print("Lesson Teachers: ")
                        for teacher_id in lesson.teacher_ids:
                            teacher = teachers.read_teacher(teacher_id)
                            print(f"{teacher.teacher_id}-{teacher.first_name} {teacher.surname}")
                        upd_teacher_id = int(input("Pick the (id) to delete: "))
                        lesson.teacher_ids.remove(upd_teacher_id)
                elif choice == 3:
                    upd_student_choice = int(input("Updating lesson students: 1-add, 2-remove: "))
                    if upd_student_choice == 1:
                        print("Students(not in lesson): ")
                        for student in students.students:
                            if student.student_id not in lesson.student_ids:
                                print(f"{student.student_id}-{student.first_name} {student.last_name}")
                        upd_student_id = int(input("Pick the (id) to add: "))
                        lesson.student_ids.append(upd_student_id)
                    elif upd_student_choice == 2:
                        print("Lesson Student: ")
                        for student_id in lesson.student_ids:
                            student = students.search_pupil_by_id(student_id)
                            print(f"{student.pupil_id}-{student.first_name} {student.last_name}")
                        upd_student_id = int(input("Pick the (id) to delete: "))
                        lesson.student_ids.remove(upd_student_id)
                break
    
    def delete_lesson(self, lesson_id):
        for i in range(len(self.lessons)):
            if lesson_id == self.lessons[i].lesson_id:
                self.lessons.pop(i)
                return
        else:
            print("No lesson with this id!")


    
