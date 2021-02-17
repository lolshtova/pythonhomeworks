with open('third.txt', 'r', encoding='UTF-8') as f:
    count = 0
    c = 0
    for line in f:
        a = line.split()
        b = float(a[1])
        count += 1
        c += b
        if float(a[1]) < 20000:
            print('оклад меньше 20 -', a[0], a[1])
    print('средняя величина дохода -', c/count)
