class User:
    achievements = property()
    __achievements = []

    def __init__(self, name, age: int):
        self.name = name
        self.age = age

    @achievements.getter
    def achievements(self):
        return self.__achievements

    @achievements.setter
    def achievements(self, item):
        # todo Написать логику добавления и проверки ачивок
        self.__achievements.append(item)
