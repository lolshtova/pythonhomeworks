class Storage:
    def __init__(self):
        self.my_storage = {}

    def add_storage(self, org):
        self.my_storage.setdefault(org.group_name(), []).append(org)

    def extract(self, name):
        if self.my_storage[name]:
            self.my_storage.setdefault(name).pop(0)


class Org:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.model} {self.price}'


class Printer(Org):

    def __init__(self, name, model, price, color):
        super().__init__(name, model, price)
        self.color = color

    def my_print(self):
        print('я печатаю')


class Scaner(Org):
    def __init__(self, name, model, price, format):
        super().__init__(name, model, price)
        self.format = format

    def scan(self):
        print('я сканирую')


class Xerox(Org):
    def __init__(self, name, model, price, pieces):
        super().__init__(name, model, price)
        self.pieces = pieces

    def copy(self):
        print('я копирую')


sklad = Storage()
scaner = Scaner('hp', 'p-321', 9000, 'a5')
sklad.add_storage(scaner)
scaner = Scaner('hp', 'p-666', 6800, 'a3')
sklad.add_storage(scaner)
printer = Printer('sony', 'i-815', 126, 2018)
sklad.add_storage(printer)
print(sklad.my_storage)
sklad.extract('Scaner')
print(sklad.my_storage)