def text():
    a = input('введите слово по-английски: ')
    lst = a.split()
    for i in lst:
        print(i.capitalize(), end=' ')


text()
