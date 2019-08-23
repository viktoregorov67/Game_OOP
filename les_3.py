""""Creator Sergey (Gefest) Romanchuk"""
import random

game_name = 'В поисках Байта'

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

player = {'name': {'question': 'Как тебя зовут?',
                   'param': {'type': str},
                   'answer': None},
          'age': {'question': 'Сколько тебе лет?',
                  'param': {'type': int,
                            'error_msg': 'вводить надо число полных лет!',
                            },
                  'answer': None},
          'sex': {'question': 'Какого ты пола? М/Ж',
                  'param': {'type': str,
                            'good': ('м', 'ж'),
                            'error_msg': 'Ваш пол надо вводить либо М либо Ж',
                            },
                  'answer': None},
          'pet_name': {'question': 'Имя твоего питомца',
                       'param': {'type': str},
                       'answer': None},
          'like_game': {'question': 'Любишь играть в игры? да/нет',
                        'param': {'type': bool,
                                  'good': ('да', 'нет'),
                                  'compliance': {'да': True, 'нет': False},
                                  'error_msg': 'Ваш пол надо вводить либо да либо нет',
                                  },
                        'answer': None}
          }


def write_to_file(**kwargs):
    with open('game_log', 'a') as file:
        for key, value in kwargs.items():
            file.write(f'{key} - {value}')


def break_game():
    print('Очень жаль, жду тебя позже')
    exit()


def cheak_age():
    if int(player['age']['answer']) < 18:
        error_print(param={'error_msg': 'Ты слишком молодой, нельзя играть'})
        break_game()

    elif int(player['age']['answer']) >= 90:
        temp_question = ('Игра может быть слишком утомительна для вас, вы уверены что желаете играть? да/нет',
                         'Хорошо подумал? да/нет',
                         )


        for itm in temp_question:
            while True:
                ask = input(itm + '\n')
                if ask.lower() == 'exit':
                    break_game()
                elif ask.lower() not in ('да', 'нет'):
                    error_print(param={'error_msg': 'неверный ввод, надо вводить да или нет'})
                    continue
                elif ask.lower() == 'да':
                    break
                else:
                    print('В другой раз, до свидания', player['name']['answer'])
                    break_game()

    return True



def error_print(**kwargs):
    print(kwargs['param']['error_msg'])


def register_user(**kwargs):
    '''
    :param kwargs:
    :return:
    '''

    for key, item in kwargs.items():
        while True:
            ask = input(item['question'] + '\n')
            if ask.lower() == 'exit':
                break_game()

            else:
                if item.get('param').get('good') and (ask.lower() not in item.get('param').get('good')):
                    error_print(**item)
                    continue
                elif item.get('param').get('type') is int:
                    if not ask.isdigit():
                        error_print(**item)
                        continue
                    ask = item.get('param').get('type')(ask)
                elif item.get('param').get('type') is bool:
                    ask = item['param']['compliance'][ask]

            item['answer'] = ask
            break


def game_not_in_alphabet():
    print('Я знаю каких букв нет в твоем имени')
    result = []
    for char in alphabet:
        if char.lower() not in player['name']['answer']:
            result.append(char.upper())

    print(f'*|{"|".join(result)}|*')


def game_where_number():
    game_strict = {

        'question': 'Я задумал 16 чисел от 1 - 16 и расположил их в произвольном порядке в строке. '
                    'Скажи мне Где какое?',
        'numbers': list(range(1, 17)),
        'for_numbers': list(range(1, 17)),
        'done_numbers': [],
        'result_string': '|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|',
        'game_step': 0,
    }
    random.shuffle(game_strict['numbers'])
    random.shuffle(game_strict['for_numbers'])
    while game_strict['for_numbers']:
        print(game_strict['question'])
        print(game_strict['result_string'])
        tmp_num = game_strict["for_numbers"][-1]
        current = game_strict['numbers'].index(tmp_num)
        ask = input(f'где число {tmp_num}?' + '\n')

        if ask.lower() == 'exit':
            break_game()

        elif ask.lower() == 'меню':
            break

        elif ask not in game_strict['numbers'] or not ask.isdigit():
            print('некоректный ввод, повторите')
            continue

        if int(ask) - 1 == current:
            print("Да действительно верно!")
            tmp_result = game_strict['result_string'].split('|')
            tmp_result[int(ask)] = tmp_num
            game_strict['result_string'] = '|'.join(tmp_result)
            game_strict['done_numbers'].append(tmp_num)
            game_strict['for_numbers'].pop()
        else:
            print('нет не верно, попробуй еще.')
        game_strict['game_step'] += 1
    else:
        print(f'ВСЕГО ХОДОВ: {game_strict["game_step"]}')


def game_rock_paper_scissors():
    game_strict = {
        'question': 'Бросай свой предмет (Камень, Ножницы, Бумага)',
        'param': {'type': str,
                  'good': ('камень', 'ножницы', 'бумага'),
                  'error_msg': 'Такого предмета нет, введи правильно',
                  },
        'results': {player['name']['answer']: 0, 'computer': 0, 'dead_heat': 0},
        'game_step': 0,
    }

    while True:
        game_strict['game_step'] += 1
        comp = random.choice(game_strict['param']['good'])
        ask = input(game_strict['question'] + '\n')
        len_name = len(player["name"]["answer"]) if len(player["name"]["answer"]) > len('computer') else len('computer')

        if ask.lower() == 'exit':
            break_game()
        elif ask.lower() == 'меню':
            break

        if ask.lower() not in game_strict['param']['good']:
            error_print(**game_strict)
            continue

        elif ask.lower() == comp:
            game_strict['results']['dead_heat'] += 1

        elif (ask.lower() == 'бумага' and comp == 'камень') or (ask.lower() == 'камень' and comp == 'ножницы') or (
                ask.lower() == 'ножницы' or comp == 'бумага'):
            game_strict['results'][player["name"]["answer"]] += 1
        else:
            game_strict['results']['computer'] += 1

        stat_info = {
            'title': f'''ход: {game_strict['game_step']}''',
            'names': f'''{player["name"]["answer"].title().center(len_name)} # {'computer'.title().center(len_name, )}''',
            'score': f'''{str(game_strict["results"][player['name']['answer']]).center(len_name)}#{str(game_strict["results"]["computer"]).center(len_name)}''',
            'footer': f''' ничьи: {game_strict["results"]["dead_heat"]} '''
        }

        max_string = len(max(stat_info.values(), key=len)) + 5

        print('#'.center(max_string))
        for key, values in stat_info.items():
            print(values.center(max_string, '#'))


def menu():
    menu_items = {
        '1': ('Каких буков нет в моем имени', game_not_in_alphabet),
        '2': ('Угадай где число', game_where_number),
        '3': ('Камень, Ножницы, Бумага', game_rock_paper_scissors),
        'exit': ('Завершить программу', break_game),
    }

    print("Главное меню")

    for key, value in menu_items.items():
        print(f'{key} - {value[0]}')
    print('#' * 10)

    while True:
        ask = input('Что выбираем?\n')

        if ask.lower() in menu_items:
            return menu_items[ask.lower()][1]
        else:
            error_print(param={'error_msg': 'неверный ввод проверьте правильность'})


if __name__ == '__main__':
    print(f'добро пожаловать в программу {game_name.upper()}')
    register_user(**player)
    start_game = cheak_age()

    while start_game:
        start = menu()
        start()
