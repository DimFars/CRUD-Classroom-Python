class Student:
    def __init__(self, first_name="", last_name="", fathers_name="", age=-1, class_name="", id_number=None, student_id=-1):
        self.first_name = first_name
        self.last_name = last_name
        self.fathers_name = fathers_name
        self.age = age
        self.class_name = class_name
        self.id_number = id_number
        self.student_id = student_id

    def __str__(self):
        det = f'\nName         : {self.first_name}'
        det += f'\nLast name    : {self.last_name}'
        det += f"\nFather's name: {self.fathers_name}"
        det += f"\nAge          : {self.age}"
        det += f"\nClass        : {self.class_name}"
        if self.id_number is not None:
            det += f"\nID number    : {self.id_number}"
        return det
        
    def from_dict(self, student_dict):
        self.first_name = student_dict["first_name"]
        self.last_name = student_dict["last_name"]
        self.fathers_name = student_dict["fathers_name"]
        self.age = student_dict["age"]
        self.class_name = student_dict["class_name"]
        if "id_number" in student_dict:
            self.id_number = student_dict["id_number"]
        self.student_id = student_dict["student_id"]

    def to_dict(self):
        student_dict = {"first_name": self.first_name,
                      "last_name": self.last_name,
                      "fathers_name": self.fathers_name,
                      "age": self.age,
                      "class_name": self.class_name,
                      "student_id": self.student_id}
        if self.id_number is not None:
            student_dict["id_number"] = self.id_number
        return student_dict