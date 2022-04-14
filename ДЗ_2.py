print('Привет! Предлагаю проверить свои знания английского!')

name = input('Расскажи, как тебя зовут! ')
print(f'Привет, {name.title()}, начинаем тренировку!')
print()
count = 0

print('My name ___ Vova')
answer = input().lower()
if answer == 'is':
    count += 1
    points = count * 10
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: is')
print()

print('I ___ a coder')
answer = input().lower()
if answer == 'am':
    count += 1
    points = count * 10
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: am')
print()

print('I live ___ Moscow')
answer = input()
if answer == 'in':
    count += 1
    points = count * 10
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: in')
print()

percent = int(points/30*100)  # корректные окончания для процентов

last_digit = percent % 10
if 11 <= last_digit <= 19:
    ending = 'процентов'
elif last_digit == 1:
    ending = 'процент'
elif 2 <= last_digit <= 4:
    ending = 'процента'
else:
    ending = 'процентов'

last_ending = count % 10      # корректные окончания для вопросов
if 11 <= last_ending <= 19:
    question = 'вопросов'
elif last_ending == 1:
    question = 'вопрос'
elif 2 <= last_ending <= 4:
    question = 'вопроса'
else:
    question = 'вопросов'

print(f'Вот и все, {name.title()}!\nВы ответили на {count} {question} из 3 верно.\nВы заработали {points} баллов.\nЭто {percent} {ending}.')