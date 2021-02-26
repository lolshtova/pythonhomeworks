class OwnError(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    try:
        a = input('введите число или stop: ')
        if a == 'stop':
            break
        my_list.append(int(a))
        print(my_list)
    except ValueError:
        print('вы ввели не число')
    except OwnError as err:
        print(err)
