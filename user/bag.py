class WeightError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return 'Невозможно поднять, слишком высокий вес'


class CellError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return 'В рюгзаке недостаточно места'


class Bag:

    def __init__(self, character):
        self.character = character
        self.__cell = 30
        self.__items = []

    @property
    def max_weight(self):
        return self.character.power * 2

    @property
    def cell(self):
        return self.__cell

    @property
    def items(self):
        return self.__items

    @property
    def weight(self):
        return sum(map(lambda x: x.weight, self.__items))

    def add_item(self, item):
        if self.weight + item.weight > self.max_weight:
            raise WeightError
        elif self.cell - item.cells < 0:
            raise CellError
        else:
            self.__items.append(item)

    def del_item(self, item):
        self.__items.remove(item)
