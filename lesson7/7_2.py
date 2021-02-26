from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def itog(self):
        pass


class Coat(Clothes):
    class_coat = 0

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size <= 0:
            self.__size = 1
        elif size > 50:
            self.__size = 50
        else:
            self.__size = size

    def itog(self):
        n = round((self.size/6.5 + 0.5), 2)
        Coat.class_coat += n
        return n


class Suit(Clothes):
    class_suit = 0

    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height <= 0:
            self.__height = 10
        elif height > 250:
            self.__height = 250
        else:
            self.__height = height

    def itog(self):
        h = self.height*2 + 0.5
        Suit.class_suit += h
        return h


a = int(input('введите размер пальто: '))
coat = Coat(a)
print('ткань на пальто', coat.itog())

b = int(input('введите рост в см: '))
suit = Suit(b)
print('ткани для костюма: ', suit.itog())
print('Общее кол-во ткани ', Coat.class_coat + Suit.class_suit)
