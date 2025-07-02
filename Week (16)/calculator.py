class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
        self.save(result)
        return result
    def subtract(self):
        result = self.num1 - self.num2
        self.save(result)
        return result
    def multiply(self):
        result = self.num1 * self.num2
        self.save(result)
        return result
    def divide(self):
            result = self.num1 / self.num2
            self.save(result)
            return result
    def save(self, result):
        self.num1 = result
    def Num2(self, new_num2):
        self.num2 = new_num2

calc = Calculator(10, 5)
print(calc.add())
calc.Num2(3)
print(calc.multiply())
calc.Num2(5)
print(calc.subtract())
calc.Num2(2)
print(calc.divide())

print(calc.num1)
print(calc.num2)