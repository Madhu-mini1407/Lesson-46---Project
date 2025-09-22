class Expression:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed"

    def display(self):
        print(f"Numbers: {self.a}, {self.b}")
        print(f"Addition: {self.add()}")
        print(f"Subtraction: {self.subtract()}")
        print(f"Multiplication: {self.multiply()}")
        print(f"Division: {self.divide()}")


if __name__ == "__main__":
    expr = Expression(20, 5)
    expr.display()
