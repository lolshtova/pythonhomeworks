with open('second.txt', 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1
        j = 0
        for i in line:
            if i == ' ':
                j += 1
        print('слов в', count, 'строке -', j+1)
    print('всего строк - ', count)
