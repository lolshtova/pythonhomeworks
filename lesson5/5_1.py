with open('first.txt', 'w', encoding='utf-8') as f:
    while True:
        a = input('введите текст: ')
        f.write(a + '\n')
        if not a:
            break
