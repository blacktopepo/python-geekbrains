def input_number(title):
    while True:
        try:
            number = float(input(title))
        except ValueError:
            print('Ошибка! Введите число.')
        else:
            return number


def print_result_division(first_number, two_number):
    """Печатает результат деления первого числа на второе"""
    try:
        print(f'{first_number} / {two_number} = ', first_number / two_number)
    except ZeroDivisionError:
        print('Делить на 0 нельзя!')


def print_user_data(first_name, second_name, year_of_bird, city, email, phone):
    """Печатает данные о пользователе"""
    print('\nЗадание второе')
    print(f'{first_name.title()} {second_name.title()}, год рождения: '
          f'{year_of_bird}, город проживания: {city}, email: {email}, '
          f'телефон: {phone}')


def get_sum_two_greatest_arguments(first_number, two_number, three_number):
    """возвращает сумму наибольших двух аргументов"""
    print('\nЗадание третье')
    array = first_number, two_number, three_number
    return sum(sorted(array)[1:])


def get_degree(x, y):
    print('\nЗадание четыре:')
    # Решение через цикл
    hard = 1
    y = abs(y)
    while y > 0:
        hard *= x
        y -= 1
    hard = 1 / hard
    # Простое
    simple = x ** y
    return hard


def get_sum_element(elements: list):
    """
    Принимает на вход список элементов, преобразует их в числа и
    возвращает кортеж состоящий из суммы полученных чисел и признак того что
    пользователь не ввёл символ q для остановки
    """
    current_sum = 0
    for element in elements:
        try:
            current_sum += float(element)
        except ValueError:
            if 'q' in element.lower():
                return current_sum, False
    return current_sum, True





def sum_input_number():
    print('\nЗадание четыре')
    sum_all_element = 0
    check_stop_sum = True

    while check_stop_sum:
        str_element = input('Введите числа через пробел для их суммирования, '
                        'введите "q" для окончания ввода '
                        'последовательности\n')
        list_element = str_element.split()
        sum_current_element, check_stop_sum = get_sum_element(list_element)
        sum_all_element += sum_current_element
        print(f'Сумма введёных всех елементов равна: {sum_all_element}')


def int_func(word: str) -> str:
    """
    Принимает слово из маленьких латинских букв и возвращает его же,
    но с прописной первой буквой
    """
    return word.title()


def six_task():
    print('\nЗадание шесть')
    print(int_func('hello'))
    input_string = 'hello my little wold.'
    output_string = ''
    # Проходимся по словам исходной строки и добавляем к новой строке слово
    # исходной строки, но уже с первой большой буквы
    for element in input_string.split():
        output_string += int_func(element) + ' '
    print(output_string)


if __name__ == '__main__':
    print('Задание первое:\nВведите два числа, для деления первого на второе')
    first, two = input_number('Первое:\n'), input_number('Второе:\n')
    print_result_division(first, two)

    # Второе
    print_user_data('alex', 'block', '1880', 'Питер', 'ablock@sp.ru','3366')

    # Третье
    print(get_sum_two_greatest_arguments(5, 3, 2))

    # Четвёртое
    print(get_degree(2, -3))
    # Пятое
    sum_input_number()
    # Шестое
    six_task()
