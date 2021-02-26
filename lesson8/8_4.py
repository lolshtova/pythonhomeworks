class Storage:
    pass


class Org:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price


class Printer(Org):
    def __init__(self, name, model, price, color):
        super().__init__(name, model, price)
        self.color = color

    def print(self):
        print('я печатаю')


class Scanner(Org):
    def __init__(self, name, model, price, quality):
        super().__init__(name, model, price)
        self.quality = quality

    def scan(self):
        print('я сканирую')


class Xerox(Org):
    def __init__(self, name, model, price, pieces):
        super().__init__(name, model, price)
        self.pieces = pieces

    def copy(self):
        print('я копирую')


a = Xerox('samsung', 'ip444', '4500', '4')
print(a.price)
a.copy()

