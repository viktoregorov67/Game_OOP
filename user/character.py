from user.bag import Bag


class Character:
    __ch_type = ('воин', 'маг')

    def __init__(self, user=None):
        self.user = user
        while True:
            question = input(f'выберите класс персонажа {" или ".join(self.__ch_type)}\n')
            if question.lower() in self.__ch_type:
                if question.lower() == 'маг':
                    self.__create_magical()
                else:
                    self.__create_warrior()
                break
            print('Неверный ввод, повторите')
        self.bag = Bag(self)

    def __create_warrior(self):
        self.power = 60
        self.heath_point = 80
        self.intelligence = 40

    def __create_magical(self):
        self.power = 30
        self.heath_point = 50
        self.intelligence = 80


if __name__ == '__main__':
    mag = Character()
