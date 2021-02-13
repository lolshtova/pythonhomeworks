class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


parent = Stationery()
parent.draw()

a = Pen()
a.draw()

b = Pencil()
b.draw()

c = Handle()
c.draw()
