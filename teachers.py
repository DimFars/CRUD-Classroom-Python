import os
import json
from teacher import Teacher


def filepath(filename):
    filepath = os.path.dirname(__file__) + "\\" + filename
    return filepath

class Teachers:
    def __init__(self):
        try:
            with open(filepath("Data_Project_CRUD_Teachers.json")) as f:
                teachers_list = json.load(f)
            self.teachers = []
            for teacher_dict in teachers_list:
                t = Teacher()
                t.from_dict(teacher_dict)
                self.teachers += [t]
        except FileNotFoundError:
            self.teachers = []

    def save_teachers_data(self):
        list_to_write = []
        for teacher in self.teachers:
                list_to_write += [teacher.to_dict()]
                
        with open(filepath("Data_Project_CRUD_Teachers.json"), "w") as f:
            json.dump(list_to_write, f)
    
    def next_id(self): #exei ena bug logikis fuseos opou ama kanw delete ena id pou den einai to teleutaio, otan kanw create den bazei to id apo tin arxi alla apo to teleutaio+1
        if not self.teachers:
            return 1001
        else:
            ids = []
            for t in self.teachers:
                ids.append(t.teacher_id)
            return max(ids) + 1

    def create_teacher(self, first_name, surname):
        for teacher in self.teachers:
            if teacher.first_name == first_name and teacher.surname == surname:
                print("Error. Teacher already exists! ")
                return None
        
        t = Teacher(first_name, surname, self.next_id())
        self.teachers.append(t)
        return t

    def read_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                return teacher
        else:
            return None
    
    def update_teacher(self, teachers_id):
        for teacher in self.teachers:
            if teachers_id == teacher.teacher_id:
                teacher.print_teacher()
                choice = int(input("Update 1-name, 2-surname: "))
                if choice == 1:
                    teacher.first_name = input("Give new name: ")
                elif choice == 2:
                    teacher.surname = input("Give new surname: ")
                return

    def delete_teacher(self, teachers_id, lessons):
        for i, __teacher_id in enumerate(self.teachers):
            if teachers_id == __teacher_id.teacher_id:
                self.teachers.pop(i)
            
                for lesson in lessons.lessons:
                    if teachers_id in lesson.teacher_ids:
                        lesson.teacher_ids.remove(teachers_id)
                return
        else:
            print("No teacher with this id")