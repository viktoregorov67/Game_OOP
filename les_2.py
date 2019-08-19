""""Creator Sergey (Gefest) Romanchuk"""

game_name = 'В поисках Байта'
break_game = False
# храним алфавит в виде строки
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# структура для хранения данных о пользователе и вопросы которые надо задать
player = {'name': {'question': 'Как тебя зовут?', 'answer': None},
          'age': {'question': 'Сколько тебе лет?', 'answer': None},
          'sex': {'question': 'Какого ты пола? М/Ж', 'answer': None},
          'pet_name': {'question': 'Имя твоего питомца', 'answer': None},
          'like_game': {'question': 'Любишь играть в игры? да/нет', 'answer': None}
          }

print("добро пожаловать в игру", game_name)

"""
для того что-бы опросить нашего пользователя и в случае расширения опроса, 
делаем цикл который пройдя по словарю будет задавать нужные вопросы  
"""
for itm in player:
    '''
    вложенный бесконечный цикл очень опасен, надо его контролировать, 
    он нужен для того что-бы снова задать вопрос если мы получим неверные данные
    '''

    while not break_game:
        # тут мы задаем вопрос добавляя перенос строки, и сохраняем во временную переменную
        temp = input(player[itm]['question'] + '\n')
        if temp.lower() == 'exit':
            break_game = True
        # преобразуем возраст в int
        if itm == 'age':
            if temp.isdigit():
                temp = int(temp)

            else:
                print('Надо вводить число')
                continue

        # проверяем пол
        elif itm == 'sex':
            # если в ответ пришло не м или ж сообщаем ошибку и запускаем цикл вопроса заново
            temp = temp.lower()
            if not (temp == 'м' or temp == 'ж'):
                print('Ваш пол надо вводить либо м либо ж')
                continue
        # тут мы проверяем ответ на да и нет, и преобразуем это в булевое значение
        elif itm == 'like_game':
            if temp.lower() == 'нет':
                temp = False
            elif temp.lower() == 'да':
                temp = True
            else:
                print('Вы должны ответить да или нет')
                continue

        # сохраняем ответ в структуру словаря
        player[itm]['answer'] = temp
        break

# Проверяем возраст более 18, и основная логика игры у нас внутри

if not break_game and player['age']['answer'] > 18:
    # данная переменая нужна что-бы учесть все ответы если пользователь очень старый для игры
    start_game = True
    if player['age']['answer'] >= 90:

        temp_question = ('Игра может быть слишком утомительна для вас, вы уверены что желаете играть? да/нет',
                         'Хорошо подумал? да/нет',
                         )

        for itm in temp_question:
            if break_game:
                break
            while start_game:
                start_game = input(itm + '\n')
                if start_game.lower() == 'да':
                    start_game = True
                elif start_game.lower() == 'нет':
                    start_game = False
                elif start_game.lower() == 'exit':
                    break_game = True
                    break
                else:
                    print('Вы должны ответить да или нет')
                    continue
                if start_game:
                    print('Хорошо тогда начнем игру')
                else:
                    print('В другой раз, до свидания', player['name']['answer'])

                break
    else:
        print('Привет', player['name']['answer'])

    if not break_game and start_game:
        print('Я могу назвать буквы алфавита которых нет в твоем имени')
        for char in alphabet:

            if char not in player['name']['answer']:
                print(char)

        game_where_number = {
            'question': 'Я задумал 16 чисел от 1 - 16 и расположил их в произвольном порядке в строке. '
                        'Скажи мне Где какое?',
            'numbers': ('1', '7', '8', '9', '3', '4', '13', '14', '5', '2', '6', '10', '11', '12', '15', '16',),
            'for_numbers': ['4', '13', '14', '5', '1', '9', '7', '8', '3', '2', '15', '16', '6', '10', '11', '12', ],
            'done_numbers': [],
            'result_string': '|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|',
            'game_step': 0,
        }

        while game_where_number['for_numbers']:
            print(game_where_number['question'])
            print(game_where_number['result_string'])
            tmp_num = game_where_number["for_numbers"][-1]
            current = game_where_number['numbers'].index(tmp_num)
            answer = input(f'где число {tmp_num}?' + '\n')

            if answer.lower() == 'exit':
                break_game = True
                break
            elif answer not in game_where_number['numbers'] or not answer.isdigit():
                print('некоректный ввод, повторите')
                continue

            if int(answer) - 1 == current:
                print("Да действительно верно!")
                tmp_result = game_where_number['result_string'].split('|')
                tmp_result[int(answer)] = tmp_num
                game_where_number['result_string'] = '|'.join(tmp_result)
                game_where_number['done_numbers'].append(tmp_num)
                game_where_number['for_numbers'].pop()
            else:
                print('нет не верно, попробуй еще.')
                continue
            game_where_number['game_step'] += 1
        else:
            if not break_game:
                print('Поздравляю с победой!')
                print(f'ВСЕГО ХОДОВ: {game_where_number["game_step"]}')

else:
    if not break_game:
        print('Тебе нельзя играть, слишком молодой')
    else:
        print("ВЫХОД ИЗ ИГРЫ")
