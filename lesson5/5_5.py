with open('fifth.txt', 'w', encoding='UTF-8') as f:
    a = input('Введите числа через пробел: ')
    f.writelines(a)
with open('fifth.txt', 'r', encoding='UTF-8') as f1:
    for line in f1:
        с = line.split()
        b = sum(map(int, с))
        print('сумма чисел = ', b)
