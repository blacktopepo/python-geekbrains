def input_month_number(title: str) -> int:
    """
    Запрашивает ввод номера месяца у пользователя
    :param title: текст сообщения, которое будет выдаваться
    пользователю при запросе ввода числа
    :return: введеное пользователем число
    """
    while True:
        try:
            number = int(input(title))
        except ValueError:
            print('Ошибка! Вы ввели не номер месяца.')
        else:
            if (number > 0) and (number < 13):
                break
            else:
                print('Вы ввели число не из диапазона 1-12!')
    return number


def input_number(title):
    while True:
        try:
            number = int(input(title))
        except ValueError:
            print('Ошибка! Введенное значение должно быть натуральным числом.')
        else:
            if number >= 0:
                break
            else:
                print('Введеное число должно быть не отрицательным')
    return number


# задание первое
def print_type_element_list(list_1: list) -> None:
    """
    Печатет тип каждого элемента в списке
    :param list_1: список, у которого необходимо узнать типы
    входящих в него элементов
    :return:
    """
    print('Задание первое:')
    for el in list_1:
        print(f'тип элемента {list_1.index(el)} - {type(el)}')


def input_list() -> list:
    """
    Отвечает за ввод списка элементов
    :return:
    """
    input_element = ''
    input_list = []
    while input_element != 'q':
        input_element = input()
        input_list.append(input_element)
    else:
        input_list.remove('q')

    return input_list


def task_two():
    print('\nЗадание второе\nВведите элементы для замены. '
          'Для окончания ввода введите "q"')
    e_list = input_list()
    len_list = len(e_list)
    # Вычисляем длину списка, чтобы исключить последний элемент из
    # обмена, при нечётной длине
    len_list = (len_list - 1, len_list)[len_list % 2 == 0]

    for i in range(0, len_list, 2):
        e_list[i], e_list[i + 1] = e_list[i + 1], e_list[i]

    print(e_list)


def task_three():
    print('\nЗадание три')
    month_number = input_month_number('Введите номер месяца\n')

    month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май',
                  'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                  'Ноябрь', 'Декабрь']

    month_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель',
                  5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь',
                  12: 'Декабрь'}

    print(f'Решение через список:\n{month_number} месяц -'
          f' {month_list[month_number - 1]}')

    print(f'Решение через словарь:\n{month_dict.get(month_number)} - '
          f'{month_number} месяц года')


def task_four():
    print('\nЗадание четыре')
    input_str = input('Введите несколько слов\n')
    output = enumerate(input_str.split(' '), 1)
    for number, element in output:
        print(number, (element, element[:10])[len(element) > 10])


def task_five():
    print('\nЗадание пять')
    my_list = [7, 5, 3, 3, 2]
    new_element = input_number(f'Введите новый элемент рейтинга {my_list}\n')
    index = 0
    for element in my_list:
        if new_element <= element:
            index = my_list.index(element)+1
    my_list.insert(index, new_element)
    print(f'{new_element} добавлен в рейтинг.\nНовый рейтинг: {my_list}')


if __name__ == '__main__':
    custom_list = [1, 'два',
                   {
                       'name': 'список',
                       'len': 3,
                       'values': [1, 2, 3]
                   },
                   (4, 8, 15, 16, 23, 42),
                   {2, 5, 10}
                   ]
    print_type_element_list(custom_list)
    task_two()
    task_three()
    task_four()
    task_five()
