# student.py
"""student detail"""
class Student:
    name: str
    age: int
    branch: str
    blood_group: str
    roll_num: int
    mobile_num: str

    def __init__(self, name: str, age: int, branch: str, blood_group: str, roll_num: int, mobile_num: str):
        self.roll_num: int = roll_num
        self.name: str = name
        self.age: int = age
        self.branch: str = branch
        self.blood_group: str = blood_group
        self.mobile_num: str = mobile_num

    def __str__(self) -> str:
        return f"Student: {self.name} (Roll No: {self.roll_num}, Branch: {self.branch})"

    def __repr__(self) -> str:
        return (f"Student(name={self.name!r}, age={self.age}, branch={self.branch!r}, "
                f"blood_group={self.blood_group!r}, roll_num={self.roll_num}, "
                f"mobile_num={self.mobile_num!r})")