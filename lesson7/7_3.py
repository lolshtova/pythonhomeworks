class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count - other.count <= 0:
            return 'разность меньше или равна 0'
        else:
            return self.count - other.count

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, in_row):
        list = ['*' for _ in range(self.count)]
        return '\n'.join([''.join(list[i:i + in_row]) for i in range(0, len(list), in_row)])


a = Cell(10)
b = Cell(11)
summa = a + b
mul = a * b
sub = a - b
div = a / b
print('сложение клеток: ', summa)
print('умножение клеток: ', mul)
print('вычитание клеток: ', sub)
print('деление клеток: ', div)

cell_1 = Cell(12)
print(f'1 клетка:\n{cell_1.make_order(5)}')
cell_2 = Cell(8)
print(f'2 клетка:\n{cell_1.make_order(5)}')
