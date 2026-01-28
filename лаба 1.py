class Calculator:
    def __init__(self, number1, number2, number3):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3
        self.__num4 = 99

    def addition(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number2 - self.number3


class Calcplus(Calculator):
    def __init__(self, number1, number2,number3):
        super().__init__(number1, number2,number3)

    def addition(self):
        return self.number1+self.number2+self.number3

    def subtraction(self):
        return self.number2-self.number1

    def multiplication(self):
        return self.number1*self.number3

    def sum(self):
        return self.number1 +self.number2+self.number3+self

a = Calculator(12, 23,12)
print(a.subtraction())


