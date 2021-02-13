class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print('машина повернула', direction)

    def show_speed(self):
        print('текущая скорость машины')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('скорость превышена')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('скорость превышена')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


speed = int(input('введите скорость '))
color = input('введите цвет ')
name = input('введите название ')
direction = input('введите направление поворота ')
a = WorkCar(speed, color, name)
a.go()
a.turn(direction)
a.stop()
a.show_speed()
print('Это полицейская машина? ', a.is_police)
