def twenty_one():
    new_lst = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
    print(new_lst)


twenty_one()
