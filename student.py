# student.py

class Student:
    name: str
    age: int
    branch: str
    blood_group: str
    roll_num: int
    mobile_num: str

    def __init__(self, name: str, age: int, branch: str, blood_group: str, roll_num: int, mobile_num: str):
        self.name: str = name
        self.age: int = age
        self.branch: str = branch
        self.blood_group: str = blood_group
        self.roll_num: int = roll_num
        self.mobile_num: str = mobile_num

    def display(self):
        print("Roll No:", self.roll_num)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print("Blood Group:", self.blood_group)
        print("Mobile No:", self.mobile_num)
        print("-" * 25)
