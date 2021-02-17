def my_gen():
    a = input('введите числа через пробел: ')
    b = a.split()
    new_lst = [b[i] for i in range(len(b)) if int(b[i]) > int(b[i-1])]
    print(new_lst)


my_gen()
