# CAR CLASS

class Car:
    """Car details of a student"""
    
    brand: str
    model: str
    car_num: str
    color: str
    year: int
    price: str

    def __init__(self, brand: str, model: str, car_number: str, color: str, year: int, price: int):
        self.brand = brand
        self.model = model
        self.car_number = car_number
        self.color = color
        self.year = year
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Car Number:", self.car_number)
        print("Color:", self.color)
        print("Year:", self.year)
        print("Price:", self.price)
