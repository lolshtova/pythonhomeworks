with open('sixth.txt', 'r', encoding='utf-8') as f:
    itog = {}
    for line in f:
        a = line.replace('(л)', '')
        b = a.replace('(пр)', '' )
        c = b.replace('(лаб)', '' )
        m = c.split()
        num = []
        for el in m:
            if el.isdigit():
                num.append(int(el))
        key = m[0]
        value = sum(num)
        itog[key] = value

    print(itog)




