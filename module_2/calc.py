from math import sqrt

class Calc():
    def __init__(self, v):
        self.v = float(v)

    def add(self, n):
        self.v += float(n)
        return self
    
    def minus(self, n):
        self.v -= float(n)
        return self

    def times(self, n):
        self.v *= float(n)
        return self
    
    def sqrt(self):
        if self.v < 0:
            raise ArithmeticError("Square root of negative value cannot be determined!")
        self.v = sqrt(self.v)
        return self

    def divide(self, n):
        if n == 0:
            raise ArithmeticError("Division by 0 is not possible!")
        self.v /= float(n)
        return self

    def modulo(self, n):
        self.v %= int(n)
        return self

    def __str__(self):
        return str(self.v)