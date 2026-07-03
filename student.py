# student.py

class Student:
    name: str
    age: int
    branch: str
    blood_group: str
    roll_num: int
    mobile_num: int

    def __init__(self, name: str, age: int, branch: str, blood_group: str, roll_num: int, mobile_num: int):
        self.name: str = name
        self.age: int = age
        self.branch: str = branch
        self.blood_group: str = blood_group
        self.roll_num: int = roll_num
        self.mobile_num: int = mobile_num

    def display(self):
        print("Roll No:", self.roll_num)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print("Blood Group:", self.blood_group)
        print("Mobile No:", self.mobile_num)
        print("-" * 25)


# ---- Create 5 students ----
s1 = Student("Hemant Pant", 19, "CSE", "O+", 1, 9876543264)
s2 = Student("Pankaj Joshi", 20, "CSE", "B+", 2, 9123456780)
s3 = Student("Rohit Chandola", 19, "CSE", "A+", 3, 9988776655)
s4 = Student("Sneha Negi", 20, "Civil", "AB+", 4, 9871234567)
s5 = Student("lucky Negi", 21, "CSE", "O-", 5, 9765432109)

# ---- Display all students ----
s1.display()
s2.display()
s3.display()
s4.display()
s5.display()