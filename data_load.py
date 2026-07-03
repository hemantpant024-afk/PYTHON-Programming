from student import Student
from bank import Bank
from car import Car

class DataLoad:
    """Load all the student related data like students, cars & bank details"""

    students: list[Student]
    bank_accounts:list[Bank]
    cars:list[Car]
    student_bank_mapping: dict[int,str]
    student_car_mapping: dict[int,str]


    def load_student_data(self) -> None:
        """Load student data"""

        s1 = Student("Hemant Pant", 19, "CSE", "O+", 1, "9876543264")
        s2 = Student("Pankaj Joshi", 18, "CSE", "B+", 2, "9123456780")
        s3 = Student("Rohit Chandola", 20, "CSE", "A+", 3, "9988776655")
        s4 = Student("Sneha Negi", 18, "Civil", "AB+", 4, "9871234567")
        s5 = Student("lucky Negi", 21, "CSE", "O-", 5, "9765432109")

        self.students.append(s1)
        self.students.append(s2)
        self.students.append(s3)
        self.students.append(s4)
        self.students.append(s5)

    def load_bank_data(self) -> None:
        """Load student data"""
        b1 = Bank("PNB", "783767853457", "tharali")
        b2 = Bank("SBI", "647384384877", "tharali")
        b3 = Bank("PNB", "783767853457", "tharali")
        b4 = Bank("HDFC", "767877375378", "Kulsari")
        b5 = Bank("SBI", "898272536755", "Dewal")

        self.bank_accounts.append(b1)
        self.bank_accounts.append(b2)
        self.bank_accounts.append(b3)
        self.bank_accounts.append(b4)
        self.bank_accounts.append(b5)

    def load_car_data(self) -> None:
        """Load Car Data"""

        c1 = Car("Toyota", "Fortuner", "UK11AB1234", "Black", 2024, "4500000")
        c2 = Car("Hyundai", "Creta", "DL01CD5678", "White", 2023, "1800000")
        c3 = Car("Maruti", "Swift", "UP03BL6634", "Red", 2022, "850000")
        c4 = Car("Mahindra", "Scorpio", "HR26CD9456", "Blue", 2024, "2200000")
        c5 = Car("Tata", "Nexon", "UK07JK7890", "Grey", 2023, "1500000")

        self.cars.append(c1)
        self.cars.append(c2)
        self.cars.append(c3)
        self.cars.append(c4)
        self.cars.append(c5)


    def load_student_bank_mapping(self) -> None:
        """Join Student and Bank data"""

        self.student_bank_mapping.update(1, "783767853457")
        self.student_bank_mapping.update(2, "647384384877")
        self.student_bank_mapping.update(3, "783767853457")
        self.student_bank_mapping.update(4, "767877375378")
        self.student_bank_mapping.update(5, "898272536755")


    def load_student_car_mapping(self) -> None:
        """Join Student and Car data"""

        self.student_car_mapping.update(1,"UK11AB1234")
        self.student_car_mapping.update(2,"DL01CD5678")
        self.student_car_mapping.update(3,"UP03BL6634")
        self.student_car_mapping.update(4,"HR26CD9456")
        self.student_car_mapping.update(5,"UK07JK7890")

    
    def load(self) -> None:
        """Loading all the student data and it's related mappings"""
        self.load_student_data()
        self.load_bank_data()
        self.load_car_data()
        self.load_student_bank_mapping()
        self.load_student_car_mapping()

