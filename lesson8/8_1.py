class Data:
    def __init__(self, new_data):
        self.new_data = new_data

    @classmethod
    def number(cls, new_data):
        b = new_data.split('-')
        int_b = [int(i) for i in b]
        return int_b

    @staticmethod
    def check(new_data):
        b = new_data.split('-')
        int_b = [int(i) for i in b]
        if 1 <= int_b[0] <= 31:
            if 1 <= int_b[1] <= 12:
                if 0 < int_b[2] <= 2021:
                    return'верная дата'
                else:
                    return'Неправильный год'
            else:
                return'Неправильный месяц'
        else:
            return 'Неправильный день'


a = input('введите дату в формате dd-mm-yy: ')
print(Data.number(a))
print(Data.check(a))
