from functools import reduce
from itertools import count, cycle
from random import randint
from sys import argv


# первое задание
def payroll_preparation():
    print('Задание первое')
    script_name, number_of_hours, rate_per_hour, bonus = argv
    try:
        payment = int(number_of_hours) * int(rate_per_hour) + int(bonus)
    except ValueError:
        print('Во входных данных вы ввели не корректные данные(ожидались '
              'числа), перезапустите программу с правильными аргументами')
    else:
        print(f'За месяц сотрудник заработал: {payment}')


# второе задание
def list_transformation():
    print('\nЗадание второе')
    original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    # добавляем дополнительную проверку для того чтобы не включать 0
    # элемент, если он больше последнего(-1)
    print([el for el in original_list
           if el > original_list[original_list.index(el) - 1]
           and (original_list.index(el) - 1) != -1])


# третье задание
def aliquot_numbers():
    print('\nЗадание третье:')
    print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])


# четвёртое задание
def print_no_repeat_elements():
    print('\nЗадание четвёртое')
    original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [el for el in original_list if original_list.count(el) == 1]
    print(result)


# Пятое задание
def five_task():
    print('\nЗадание пятое')
    result = [el for el in range(100, 1001, 2)]
    print(reduce(lambda el_1, el_2: el_1 * el_2, result))


def six_task():
    print('\nЗадание шестое')
    print('итератор, генерирующий целые числа, начиная с указанного,')
    result_1 = []
    for el in count(3):
        if el > 10:
            break
        else:
            result_1.append(el)
    print(result_1)
    print('\nитератор, повторяющий элементы некоторого списка, '
          'определенного заранее.')

    result_2 = []
    # Будет выполняться пока не count_param не станет больше либо равен
    # рандомному числу от 0 до 100
    count_param = 0
    stint = randint(0, 100)
    for el in cycle([10, 5, 1, 3, 2]):
        if count_param >= stint:
            break
        result_2.append(el)
        count_param += 1
    print(result_2)


def generator_sequence(n: int):
    for current in range(1, n+1):
        yield current


def seven_task():
    print('\nЗадание седьмое')
    n = 4
    g = generator_sequence(n)
    factorial_n = 1
    for el in g:
        factorial_n *= el
    print(f'Факториал {n} = {factorial_n}')


if __name__ == '__main__':
    payroll_preparation()
    list_transformation()
    aliquot_numbers()
    print_no_repeat_elements()
    five_task()
    six_task()
    seven_task()
