import random


class Location:

    def __init__(self, left: bool, right: bool, up: bool, down: bool):
        self.__items = []
        self.left = left
        self.right = right
        self.up = up
        self.down = down


class Map:
    def __init__(self, x, y):
        self.__map = [[None for _ in range(x)] for _ in range(y)]
        self.__generate_location()

    def __generate_location(self):
        for idx, line in enumerate(self.__map):
            for ids, itm in enumerate(line):
                not_walls = [False, True, False, True]
                if not idx and not ids:
                    random.shuffle(not_walls)
                    line[ids] = Location(*not_walls)

                elif ids <= len(line) - 1:

                    for enum, num in enumerate(not_walls):
                        if not enum:
                            not_walls[enum] = self.__get_left(idx, ids)
                        elif enum == 1:
                            not_walls[enum] = self.__get_right(idx, ids)
                        elif enum == 2:
                            not_walls[enum] = self.__get_up(idx, ids)
                        elif enum == 3:
                            not_walls[enum] = self.__get_up(idx, ids)

                    line[ids] = Location(*not_walls)

    def __get_left(self, x, y):
        try:
            if not self.__map[x][y - 1].left:
                return self.__map[x][y - 1].left
        except IndexError:
            pass
        except AttributeError:
            pass
        return random.choice([True, False, True])

    def __get_right(self, x, y):
        try:
            if not self.__map[x][y - 1].right:
                return self.__map[x][y - 1].right
        except IndexError:
            pass
        except AttributeError:
            pass
        return random.choice([True, False, True])

    def __get_up(self, x, y):
        try:

            if not self.__map[x][y - 1].up:
                return self.__map[x][y - 1].up
        except IndexError:
            pass
        except AttributeError:
            pass
        return random.choice([True, False, True])

    def __get_down(self, x, y):
        try:

            if not self.__map[x][y - 1].down:
                return self.__map[x][y - 1].down
        except IndexError:
            pass
        except AttributeError:
            pass
        return random.choice([True, False, True])



if __name__ == '__main__':
    loc_map = Map(10, 10)
    print(1)
