from data_load import DataLoad
from student import Student
from bank import Bank
from car import Car

class StudentService:

    def find_student_details(self, roll_num: int, students: list[Student]) -> Student:
        """Find Student Data Based on Roll Number"""

        student: Student = None
        for s in students:
            if roll_num == s.roll_num:
                student = s
                break
        return student
        
    
    def find_car_details(self, car_num: str, cars: list[Car]) -> Car:
        """Finds Car details by Car Number"""

        car: Car = None
        for c in cars:
            if car_num == c.car_number:
                car = c
                break

        return car
    

    def find_bank_details(self, account_num: str, bank_details: list[Bank]) -> Bank:
        """Find Bank details by account number"""

        bank: Bank = None

        for b in bank_details:
            if account_num == b.account_number:
                bank = b
                break
        
        return bank


    def get_bank_account_number(self, roll_number: int, student_bank_mapping: dict[int, str]) -> str:
        """Get Bank account number by Student roll number"""
        return student_bank_mapping[roll_number]
    
    def get_car_number(self, roll_number: int, student_car_mapping: dict[int, str]) -> str:
        """Get Car number by Student roll number"""
        return student_car_mapping[roll_number]

