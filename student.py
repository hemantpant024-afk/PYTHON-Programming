# student.py

class Student:
    name: str
    age: int
    course: str
    blood_group: str
    roll_num: int
    is_hostilier: bool

    def display(self):
        print("Student Details")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Course :", self.course)


# Create an object
student1 = Student()

# Assign values
student1.name = "Hemant"
student1.age = 19
student1.course = "CSE"

# Display details
student1.display()
