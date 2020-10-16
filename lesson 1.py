# Хелперы
def get_two_signs(number):
    if number < 10:
        number = '0' + str(number)
    return number


def input_number(title, type_number=int):
    while True:
        try:
            number = type_number(input(title))
        except ValueError:
            print('Ошибка! Вы ввели не целое число.')
        else:
            if number >= 0:
                break
    return number


# второе
def second_to_time():
    number_of_second = input_number('Введите количество секунд:\n')
    hh = get_two_signs(number_of_second // 3600)
    number_of_second = number_of_second % 3600
    mm = get_two_signs(number_of_second // 60)
    ss = get_two_signs(number_of_second % 60)
    return f"{hh}:{mm}:{ss}"


# третье
def triple_number():
    n = input_number("Введите число n. Для нахождения суммы чисел n + nn + "
                     "nnn\n")
    return n + (n*10+n) + (n*100 + n*10 + n)


def get_max_number():
    number = input_number('Введите целое положительное число\n')
    max_numeric = 0
    while number > 0:
        numeric = number % 10
        number //= 10
        if numeric > max_numeric:
            max_numeric = numeric
    return max_numeric


def calculate_profitability():
    proceeds = input_number('Введите выручку фирмы\n', float)
    costs = input_number('Введите издержки фирмы\n', float)
    if costs > proceeds:
        print('Фирма работает в убыток =(')
    elif costs == proceeds:
        print('Фирма работает в 0')
    else:
        profit = proceeds-costs
        print(f'Прибыль составила {profit}')
        print(f'Рентабельность составляет: {profit/proceeds}')
        employees_number = input_number('Введите численность сотрудников '
                                        'фирмы\n', int)
        print(f'Один сотрудник приносит фирме {profit / employees_number}')


def calculate_day():
    current = input_number('Введите текущий показатель\n', int)
    target = input_number('Введите желаемый показатель\n', int)
    count = 1
    while current < target:
        current *= 1.1
        count += 1
    print(f'на {count}-й день спортсмен достиг результата — '
          f'не менее {target} км')


if __name__ == '__main__':
    print('Задание второе:\nПользователь вводит время в секундах. '
          'Переведите время в часы, минуты и секунды и выведите в формате '
          'чч:мм:сс. Используйте форматирование строк.')
    print(second_to_time())

    print('Задание третье:\nУзнайте у пользователя число n. Найдите сумму '
          'чисел n + nn + nnn. Например, пользователь ввёл число 3. '
          'Считаем 3 + 33 + 333 = 369')
    print(triple_number())
    print('Задание четвертое:\nПользователь вводит целое положительное число. '
          'Найдите самую большую цифру в числе.')
    print(get_max_number())
    print('Задание пятое:\nЗапросите у пользователя значения выручки и '
          'издержек фирмы. Определите, с каким финансовым результатом '
          'работает фирма')
    calculate_profitability()
    print('Задание шесть\nРасчёт дня достижения результата спортсменом')
    calculate_day()
