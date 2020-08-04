class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumbers(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + other.a * self.b
        return ComplexNumbers(a, b)

    def __str__(self):
        return f"({self.a}+{self.b}i)" if self.b > 0 else f"({self.a}-{abs(self.b)}i)"


x = ComplexNumbers(12, 5)
y = ComplexNumbers(66, 2)
print(x)
print(y)
print(x + y)
print(x * y)
