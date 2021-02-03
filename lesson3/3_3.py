def my_func(x, y, z):
    lst = [x, y, z]
    rmv_element = min(lst)
    if rmv_element in lst:
        lst.pop(lst.index(rmv_element))
        a = lst[0]+lst[1]
        return a


x = int(input('введите х: '))
y = int(input('введите y: '))
z = int(input('введите z: '))
print(my_func(x, y, z))
