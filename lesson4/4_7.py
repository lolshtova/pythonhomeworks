def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    yield f

    n = int(input('введите число: '))
for el in fact(n):
    print(el)
