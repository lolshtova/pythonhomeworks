class OwnError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b


a = int(input('введите делимое: '))
b = int(input('введите делитель: '))

try:
    res = round((a / b), 2)
except ZeroDivisionError:
    print('деление на ноль')
else:
    print(f'Итого {res}')
finally:
    print('The end!')
