class Road:
    def __init__(self, __length, __width):
        self.length = __length
        self.width = __width

    def formula(self):
        massa = int(input('Введите массу асфальта: '))
        sloi = int(input('введите толщину полотна: '))
        return self.length * self.width * massa * sloi / 1000


road = Road(20, 5000)
print(road.formula(), 'тысяч')
