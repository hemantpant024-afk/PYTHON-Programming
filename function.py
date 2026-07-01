class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self.value

    def subtract(self, x):
        self.value -= x
        return self.value

    def reset(self):
        self.value = 0
        return self.value


# Usage
calc = Calculator()
print(calc.add(10))       # 10
print(calc.subtract(3))   # 7
print(calc.reset())       # 0