def my():
    x = input('введите числа разделенные пробелами: ')
    b = x.split(' ')
    a = 0
    for i in b:
        i = int(i)
        a += i
    print(a)
    while True:
        y = input('введите числа разделенные пробелами: ')
        if y == 'stop':
            print(m)
            return
        c = y.split(' ')
        b.extend(c)
        m = 0
        for j in b:
            j = int(j)
            m += j
        print(m)


my()
