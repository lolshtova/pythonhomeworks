class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = _income


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self.income.get('wage')+self.income.get('bonus'))


name = input('введите имя: ')
surname = input('введите фамилию: ')
position = input('введите должность: ')
wage = int(input('введите оклад: '))
bonus = int(input('введите премию: '))
_income = {'wage': wage, 'bonus': bonus}
a = Position(name, surname, position, _income)
a.get_full_name()
a.get_total_income()
