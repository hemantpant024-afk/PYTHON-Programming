# CAR CLASS

class Car:
    """Car details of a student"""

    brand: str
    model: str
    car_number: str
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

    def __str__(self) -> str:
        return f"{self.color} {self.brand} {self.model} ({self.year}) - No: {self.car_number}"

    def __repr__(self) -> str:
        return (f"Car(brand={self.brand!r}, model={self.model!r}, car_num={self.car_number!r}, "
                f"color={self.color!r}, year={self.year}, price={self.price!r})")
