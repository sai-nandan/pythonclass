class Calculator:
    def __init__(self):
        self.a = 6
        self.b = 3
    def addition(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
    def subtract(self,a,b):
        return a-b
    def divide(self,a,b):
        return a/b
c = Calculator()
res = c.addition(2,3)
res = c.multiply(2,3)
res = c.subtract(2,3)
res = c.divide(2,3)