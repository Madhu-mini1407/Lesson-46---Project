class Expression:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        return self.a + self.b + self.c

    def subtract(self):
        return self.a - self.b - self.c

    def multiply(self):
        return self.a * self.b * self.c

    def divide(self):
        if self.b != 0:
            return self.a / self.b/ self.c
        else:
            return "Division by zero is not allowed"

    def display(self):
        print(f"Numbers: {self.a}, {self.b},{self.c}")
        print(f"Addition: {self.add()}")
        print(f"Subtraction: {self.subtract()}")
        print(f"Multiplication: {self.multiply()}")
        print(f"Division: {self.divide()}")


if __name__ == "__main__":
    expr = Expression(20, 5,2)
    expr.display()
