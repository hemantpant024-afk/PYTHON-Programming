# CAR CLASS

class Car:
    brand: str
    model: str
    color: str
    year: int
    price: float
    is_available: bool

    def display(self):
        print("Car Details")
        print("Brand        :", self.brand)
        print("Model        :", self.model)
        print("Color        :", self.color)
        print("Year         :", self.year)
        print("Price        :", self.price)
        print("Available    :", self.is_available)


# Create an object
c1 = Car()

# Assign values
c1.brand = "BMW"
c1.model = "BMW M3 E90 COMPETITION"
c1.color = "Black"
c1.year = 2014
c1.price = 13000000       #in ₹
c1.is_available = True

# Display details
c1.display()