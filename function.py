class Calculator:
    """A simple class to demonstrate OOP and defining methods."""
    
    def __init__(self, brand_name):
        # This is the constructor. It initializes instance attributes.
        self.brand = brand_name

    def greet_user(self):
        """A simple method with no parameters (besides self)."""
        print(f"Welcome to your {self.brand} calculator!")

    def add_numbers(self, num1, num2):
        """A method that takes parameters and returns a value."""
        result = num1 + num2
        return result


# --- How to use the class and its functions (methods) ---

# 1. Create an object (instance) of the class
my_calc = Calculator(brand_name="Casio")

# 2. Call a method that performs an action
my_calc.greet_user()

# 3. Call a method that takes arguments and returns a value
sum_result = my_calc.add_numbers(15, 25)
print(f"The sum is: {sum_result}")