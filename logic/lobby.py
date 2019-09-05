from user.user import User


class Lobby:

    def __init__(self):
        self.user = None

    def reg_user(self):
        question = {'name': {'q': 'Ваше имя?', 'ans': ''},
                    'age': {'q': 'Ваш возраст?', 'ans': 0},
                    }
        for key, quest in question.items():

            while True:
                tmp = input(f"{quest.get('q')}\n")
                if key == 'age' and not tmp.isdigit():
                    print('Возраст необходимо ввести числом')
                    continue
                elif key == 'age' and tmp.isdigit():
                    tmp = int(tmp)
                quest['ans'] = tmp
                break

        self.user = User(question['name']['ans'], question['age']['ans'])
