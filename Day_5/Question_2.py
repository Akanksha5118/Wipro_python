# Base Class
class Calculator:
    def calculate(self, a, b):
        return a + b

# AdvanceCalculator that overrides a method
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        # overriding the method
        return a * b


# Operator Overloading
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print(self.value)

# Polymorphism demonstration
calc = Calculator()
adv_calc = AdvancedCalculator()

print("Calculator result:", calc.calculate(5, 3))        # Addition
print("AdvancedCalculator result:", adv_calc.calculate(5, 3))  # Multiplication



n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2
n3.display()