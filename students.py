import os
import json
from student import Student


def filepath(filename):
    filepath = os.path.dirname(__file__) + "\\" + filename
    return filepath

class Students:
    def __init__(self):
        try:
            with open(filepath("Data_Project_CRUD_Students.json")) as f:
                students_list = json.load(f)
            self.students = []
            for student_dict in students_list:
                s = Student()
                s.from_dict(student_dict)
                self.students += [s]
        except FileNotFoundError:
            self.students = []
    
    def __str__(self):
        det = ""
        for student in self.students:
           det += "\n" + "=" * 15
           det += str(student)
        return det

    def save_students_data(self):
        list_to_write = []
        for student in self.students:
            list_to_write += [student.to_dict()]

        with open(filepath("Data_Project_CRUD_Students.json"), "w") as f:
            json.dump(list_to_write, f)
    
    def next_id(self):
        if not self.students:
            return 1001
        else:
            ids = []
            for s in self.students:
                ids.append(s.student_id)
            return max(ids) + 1
        
    def create_student(self):
        first_name = input("Give name: ")
        last_name = input("Give surname: ")
        fathername = input("Give fathername: ")

        for s in self.students:
            if first_name==s.first_name and last_name==s.last_name and fathername==s.fathers_name:
                print("This student already exists.")
                ch = input("Do you want to continue? (y-yes) (n-no) ")
                if ch=="n":
                    return None  #otan 8elw na epistrepsw to tpt alla sti sugkekrimeni periptwsi to xrisimopoio gia na
                                 #stamatisw ton atermona bronxo tis main xwris na balw break

        age = int(input("Give age: "))
        student_class = int(input("Give class: "))
        id_card = input("Does he/she has an id card (y-yes) (n-no): ")
        if id_card=="y":
            id_number = input("Give id number: ")
        else:
            id_number = None

        student = Student(first_name, last_name, fathername, age, student_class, id_number, self.next_id())
    
        self.students.append(student)
        return student
    
    def search_student_by_id(self, student_id):
        for student in self.students:
            if student_id == student.student_id:
                return student
        return None
    
    def search_student_by_surname(self, last_name):
        match_student = []
        for student in self.students:
            if last_name==student.last_name:
                match_student.append(student)
        return match_student
    
    def student_update(self, student):
        print(student)
        print("=" * 15)
        print("1-name")
        print("2-surname")
        print("3-father's name")
        print("4-age")
        print("5-class")
        print("6-id number")
        print("=" * 15)
        update_choice = int(input("Pick something to update: "))
        if update_choice == 1:
            student.first_name = input("Give new name: ")
        elif update_choice == 2:
            student.last_name = input("Give new surname: ")
        elif update_choice == 3:
            student.fathers_name = input("Give new father's name: ")
        elif update_choice == 4:
            student.age = input("Give new age: ")
        elif update_choice == 5:
            student.class_name = input("Give new class: ")
        elif update_choice == 6:
            student.id_number = input("Give new id number: ")

        print("=" * 15)
        print(student)
        print("Student updated! ")

    def delete_student_by_id(self, student_id, lessons):
        for i, student in enumerate(self.students):
            if student_id == student.student_id:
                self.students.pop(i)
                print("Student deleted")
                for lesson in lessons.lessons:
                    if student_id in lesson.student_ids:
                        lesson.student_ids.remove(student_id)
                return
        else:
            print('No student with this id')
    
    def print_students_names(self):
        for student in self.students:
            print(f'{student.first_name} {student.fathers_name[0]} {student.last_name}')
