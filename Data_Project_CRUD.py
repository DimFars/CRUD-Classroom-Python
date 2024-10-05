from student import Student
from students import Students
from teacher import Teacher
from teachers import Teachers
from lesson import Lesson
from lessons import Lessons

def choice(boundary1, boundary2):
        while True:
            choice = input("Choose one of the above: ")
            if choice.isnumeric() and boundary1<=int(choice)<=boundary2:
                return int(choice)
            else:
                print(f"{boundary1} to {boundary2}, please")

def main():
    print("Start")
    students = Students()
    teachers = Teachers()
    lessons = Lessons()

    while True:
        print("\n=================")
        print("       MENU       ")
        
        print("1 - Manage Students")
        print("2 - Manage Teachers")
        print("3 - Manage Lessons")
        print("4 - Exit")
        main_choice = choice(1, 4)
        
        
        if main_choice==1:
            print("\n===============")
            print(" STUDENTS MENU ")
            print("1 - Create Student")
            print("2 - Print Students")
            print("3 - Update Student")
            print("4 - Delete Student")
            print("5 - Exit")
            student_choice = choice(1, 5)
        
            if student_choice==1:
                print("New student".title())
                print("==========")
                student = students.create_student()
                if student is None:
                    continue
                else:
                    print("------New Student------")
                    print(student)
            
            elif student_choice==2:
                print("\n===============")
                print("       SUB-MENU (Print)       ")
                print("1 - Print Student")
                print("2 - Print all")
                print("3 - Print only Students' names")
                print("4 - Exit Print")
                print_choice = choice(1, 4)

                if print_choice==1:
                    student_id = int(input("Give ID: "))
                    student = students.search_student_by_id(student_id)
                    if student is None:
                        print("There is no student with this ID")
                    else:
                        print(student)

                elif print_choice==2:
                    print(students)
                elif print_choice==3:
                    students.print_students_names()
                else:
                    continue

            elif student_choice==3:
                print("\n===============")
                print("       SUB-MENU (Update)       ")
                print("1 - Update Student (search by id)")
                print("2 - Update Student (search by surname)")
                print("3 - Exit Update")
                update_choice = choice(1, 3)

                if update_choice==1:
                    student_id = int(input("Give ID: "))
                    student = students.search_student_by_id(student_id)
                    if student is None:
                        print("There is no student with this ID")
                        continue    
                elif update_choice==2:
                    surname = input("Give surname: ")
                    matching_students = students.search_student_by_surname(surname)
                    if not matching_students:
                        print("There is not a student matching those criteria")
                        continue
                    elif len(matching_students)==1:
                        student = matching_students[0]
                    else:
                        for i in matching_students:
                            print(f"ID = {i['id']}")
                            print("=" * 15)
                        student_id = int(input("Which ID you want: "))
                        student = students.search_student_by_id(student_id)
                else:
                    continue
                # student update
                students.student_update(student)

            elif student_choice==4:
                print("\n===============")
                print("       SUB-MENU (Delete)       ")
                print("1 - Delete Student (search by id)")
                print("2 - Delete Student (search by surname)")
                print("3 - Exit Delete")
                delete_choice = choice(1, 3)

                if delete_choice==1:
                    student_id = int(input("Give ID: "))
                    student = students.search_student_by_id(student_id)
                    if student is None:
                        print("There is no student with this ID")
                        continue    
                elif delete_choice==2:
                    surname = input("Give surname: ")
                    matching_students = students.search_student_by_surname(surname)
                    if not matching_students:
                        print("There is not a student matching those criteria")
                        continue
                    elif len(matching_students)==1:
                        student = matching_students[0]
                    else:
                        for i in matching_students:
                            print(f"ID = {i['id']}")
                            print("=" * 15)
                        student_id = int(input("Which ID you want: "))
                        student = students.search_student_by_id(student_id)
                else:
                    continue
                # student update
                students.delete_student_by_id(student.student_id, lessons)
            else:
                continue

        elif main_choice==2:
            print("\n===============")
            print(" TEACHERS MENU ")
            print("1 - Create Teacher")
            print("2 - Print Teacher")
            print("3 - Update Teacher")
            print("4 - Delete Teacher")
            print("5 - Exit")
            teacher_choice = choice(1, 5)

            if teacher_choice==1:
                first_name = input("Write name: ")
                surname = input("Write surname: ")
                teachers.create_teacher(first_name, surname)
        
            elif teacher_choice==2:
                teachers_id = int(input("Write id: "))
                teacher = teachers.read_teacher(teachers_id)
                if teacher is None:
                    print("No such teacher exists!")
                else:
                    print(teacher)
            
            elif teacher_choice==3:
                teacher_id = int(input("Write id: "))
                teachers.update_teacher(teacher_id)

            elif teacher_choice==4:
                teacher_id = int(input("Write id to delete: "))
                teachers.delete_teacher(teacher_id, lessons)
                
            else:
                continue
        elif main_choice==3:
            print("\n===============")
            print(" LESSONS MENU ")
            print("1 - Create Lesson")
            print("2 - Print Lesson")
            print("3 - Update Lesson")
            print("4 - Delete Lesson")
            print("5 - Exit")
            lesson_choice = choice(1, 5)

            if lesson_choice==1:
                lesson_name = input("Give lesson name: ")
                lessons.create_lesson(lesson_name)
            elif lesson_choice==2:
                lesson_id = int(input("Give id: "))
                lesson = lessons.read_lesson(lesson_id)
                if lesson is None:
                    print("No such lesson exists!")
                else:
                    lesson.print_lesson_details(teachers, students)
            elif lesson_choice == 3:
                lesson_id = int(input("Give id: "))
                lessons.update_lesson(lesson_id, teachers, students)
            elif lesson_choice == 4:
                lesson_id = int(input("Give id: "))
                lessons.delete_lesson(lesson_id)
            else:
                continue

        else:
            print("Bye Bye")
            students.save_students_data()
            teachers.save_teachers_data()
            lessons.save_lessons_data()
            break


main()