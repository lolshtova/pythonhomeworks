from itertools import cycle

x = int(input('введите число: '))
z = int(input('введите число для останова: '))
b = list(range(x))

i = 0
for el in cycle(b):
    print(el)
    i += 1
    if i > z-1:
        break
