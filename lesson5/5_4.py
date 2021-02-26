newf = open('file_new.txt', 'w', encoding='utf-8')
with open('four.txt', 'r', encoding='utf-8') as f:
    for line in f:
        l1 = line.replace('One', 'Один')
        l2 = l1.replace('Two', 'Два')
        l3 = l2.replace('Three', 'Три')
        l4 = l3.replace('Four', 'Четыре')
        newf.write(l4)
newf.close()
