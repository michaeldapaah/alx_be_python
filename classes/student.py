class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
student = Student("John Doe", 20)
student2 = Student("Jane Smith", 22)
print(student.student_info())
print(student2.student_info())

