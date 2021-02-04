def separet(x, y):
    c = x/y
    return c


x = int(input('введите х: '))
y = int(input('введите y: '))
try:
    separet(x, y)
except ZeroDivisionError:
    print('деление на ноль')
print(separet(x, y))
