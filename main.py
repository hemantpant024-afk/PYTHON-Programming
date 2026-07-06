from data_load import DataLoad
from student import Student
from bank import Bank
from car import Car
from student_service import StudentService

class Main:

    def __init__(self):
        self.data_load: DataLoad = DataLoad()
        self.data_load.load()
        self.student_service = StudentService()

    def print_student_details(self, roll_num: int) -> None:
        """Print Student details, like Student info, Bank details, Car details"""

        student: Student = self.student_service.find_student_details(roll_num=roll_num, students=self.data_load.students)
        car_number: str = self.student_service.get_car_number(roll_number=roll_num, student_car_mapping=self.data_load.student_car_mapping)
        car: Car = self.student_service.find_car_details(car_num=car_number, cars=self.data_load.cars)
        account_number: str = self.student_service.get_bank_account_number(roll_number=roll_num, student_bank_mapping=self.data_load.student_bank_mapping)
        bank: Bank = self.student_service.find_bank_details(account_num=account_number, bank_details=self.data_load.bank_accounts)


        print(f"Student Data: {student}")
        print(f"Car Details:: {car}")
        print(f"Bank Details:: {bank}")

    
    def run(self):
        print("Staring Main...")
        roll_num: int = 3

        self.print_student_details(roll_num=roll_num)



if __name__ == "__main__":
    Main().run()
