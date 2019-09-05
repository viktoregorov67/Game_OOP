import random


class Item:
    weight = property()
    cells = property()

    def __init__(self, weight, cells):
        self.__weight = weight
        self.__cells = cells

    @weight.getter
    def weight(self):
        return self.__weight

    @cells.getter
    def cells(self):
        return self.__cells


class Weapon(Item):
    __w_type = {
        'Меч': (5, 3, 40, 'PO'),
        'Секира': (7, 5, 50, 'PO'),
        'Посох': (3, 5, 50, 'INT'),
        'Волшебная палочка': (2, 3, 60, 'INT'),
    }

    def __init__(self, name, weight, cells, demand, w_type):
        if name not in Weapon.__w_type.keys():
            raise TypeError
        self.__name = name
        self.__demand = demand
        self.__demand_type = w_type

        Item.__init__(self, weight, cells)

    @classmethod
    def create(cls):
        name = random.choice(tuple(cls.__w_type.keys()))
        params = cls.__w_type.get(name)
        return Weapon(name, *params)

    @property
    def name(self):
        return self.__name

    @property
    def demand(self):
        return self.__demand

    @property
    def demand_type(self):
        return self.__demand_type


class Thing(Item):
    __th_type = {'Рубин': (2, 1), 'Монета': (1, 1)}

    def __init__(self, name, weight, cells):
        if name not in Thing.__th_type.keys():
            raise TypeError

        self.__name = name
        Item.__init__(self, weight, cells)

    @classmethod
    def create(cls):
        name = random.choice(tuple(cls.__th_type.keys()))
        params = cls.__th_type.get(name)
        return Thing(name, *params)


if __name__ == '__main__':
    wep = Weapon.create()
    print(1)
