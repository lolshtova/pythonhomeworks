import cmath
j = cmath.sqrt(-1)


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'комплексное число {self.real}+{self.imag}j'

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return f'сумма равна {new_real}+{new_imag}j'

    def __mul__(self, other):
        mul_real = self.real * other.real - self.imag*other.imag
        mul_imag = self.imag * other.real + self.real * other.imag
        return f'произведение равно {mul_real}+{mul_imag}j'


number_1 = ComplexNumber(3, 6)
number_2 = ComplexNumber(4, -7)
sum_number = number_1 + number_2
mul_number = number_1 * number_2
print(number_1)
print(sum_number)
print(mul_number)
