gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': '',
         'pet_name': '',
         }

if gamer['age'] < 18:
    if gamer['name'] == 'Вася':
        print(gamer['name'], 'тубу нельзя играть, потому что ты Вася и молодой')
    else:
        print('Тебе нельзя играть')
elif gamer['name'] == 'Петя':
    print('Ты плохой')
else:
    print('Добро пожаловать в Игру')

print('Я могу сосчитать твой возраст')

i = 0
while i <= gamer['age']:
    print(i)
    i += 1

    if i > 22:
        print('замучился считать')
        break
else:
    print('Сработал else в цикле')

print('А еще я могу произнести имя по буквам')

i = 0
for char in gamer['name']:
    i += 1
    if i == 3:
        continue
    print(char)
