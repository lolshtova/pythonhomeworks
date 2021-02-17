def stepen(x : float, y : int):
    a = x ** y
    b = -y
    c = 1
    for j in range(b):
        c *= x
    return a, 1/c


x = int(input('введите действительное положительное x: '))
y = int(input('введите  целое отрицательное число y: '))
print(stepen(x, y))
