from random import randint
print('Здравствуйте! Это игра "Угадай число". Попробуйте угадать целое число от 1 до 100. Вы готовы?')
answer = input('Пожалуйста, введите свой ответ. Если Вы хотите продолжить - введите "да", если вы хотите выйти из игры - введите "в": ').lower()
if answer == 'yes' or answer == ' yep' or answer == 'of course' or answer == 'y' or answer == 'да' or answer == 'ад' or answer == 'д' or answer == 'ага' or answer == 'угу':
    print('Oтлично! Давайте начнем)')
elif answer == 'q' or answer == 'no' or answer == 'e' or answer == 'нет' or answer == 'неа' or answer == 'в' or answer == 'вых' or answer == 'выход' or answer == 'выйти' or answer == 'закрыть' or answer == 'зак':
    print('Очень жаль. Увидимся позднее)')
    exit()

name = input('Пожалуйста, введите своё имя: ')
number = randint(1, 100)
number_of_attempts = 1
while True:
    user_number = int(input(f'{name}, пожалуйста, введите предполагаемое число от 1 до 100: '))
    if 101 > user_number > number > 0:
        if user_number - number < 10:
            print('Число немного больше, чем нужно. Вы близко)')
            number_of_attempts += 1
        else:
            print('Число слишком большое. Попробуйте ещё.')
            number_of_attempts += 1
    elif 0 < user_number < number < 101:
        if number - user_number < 10:
            print('Число немного меньше, чем нужно. Вы близко)')
            number_of_attempts += 1
        else:
            print('Число слишком маленькое. Попробуйте ещё.')
            number_of_attempts += 1
    elif user_number == number:
        if number_of_attempts < 5:
            print(f'Вы абсолютно правы! Количество попыток: {number_of_attempts}! Это просто невероятно! Поздравляем!')
            question = input('Для выхода из игры введите "в": ').lower()
            if question == 'q' or question == 'y' or question == 'yes' or question == 'в' or question == 'вых' or question == 'выход' or question == 'выйти' or question == 'закрыть' or question == 'зак' or question == 'д' or question == 'ад' or question == 'да':
                print('Очень жаль. Увидимся позднее)')
                break
            else:
                number = randint(1, 100)
                number_of_attempts = 1
                continue
        elif number_of_attempts < 10:
            print(f'Вы абсолютно правы! Количество попыток: {number_of_attempts}! Отличная работа! Поздравляем!')
            question = input('Для выхода из игры введите "в": ').lower()
            if question == 'q' or question == 'y' or question == 'yes' or question == 'в' or question == 'вых' or question == 'выход' or question == 'выйти' or question == 'закрыть' or question == 'зак' or question == 'д' or question == 'ад' or question == 'да':
                print('Очень жаль. Увидимся позднее)')
                break
            else:
                number = randint(1, 100)
                number_of_attempts = 1
                continue
        else:
            print(f'Вы абсолютно правы! Количество попыток: {number_of_attempts}! Поздравляем!')
            question = input('Для выхода из игры введите "в": ').lower()
            if question == 'q' or question == 'y' or question == 'yes' or question == 'в' or question == 'вых' or question == 'выход' or question == 'выйти' or question == 'закрыть' or question == 'зак' or question == 'д' or question == 'ад' or question == 'да':
                print('Очень жаль. Увидимся позднее)')
                break
            else:
                number = randint(1, 100)
                number_of_attempts = 1
                continue
    elif user_number > 100:
        print('Введёное Вами число больше 100. Пожалуйста, введите новое число от 1 до 100.')
        number_of_attempts += 1
    elif 0 > user_number:
        print('Введёное Вами число меньше 1. Пожалуйста, введите новое число от 1 до 100.')
        number_of_attempts += 1