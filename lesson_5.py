import json
import re
from functools import reduce
from random import randint


def input_user_data():
    """Возвращает в строке введеные данные пользователем"""
    input_data = ' '
    output_data = ''
    while input_data:
        input_data = input()
        output_data += input_data + '\n'
    return output_data


def output_in_file():
    """Запрашивает данны у пользователя с клавиатуры и сохраняет их
    построчнов файл"""
    print('Задание 1. Введите строки, которые надо записать в файл, пустая '
          'строка - окончание ввода')
    with open('task_1.txt', 'w', encoding='utf-8') as file:
        file.write(input_user_data())
        print(f'Данные пользователя записаны в файл {file.name}')


def read_file(file_name: str) -> list:
    """
    Считывает данные из файл в список строк
    :param file_name: имя файла
    :return: данные файла
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_data = file.readlines()
    except FileNotFoundError:
        print(f'Кто то похерил файл {file_name}')
        return []
    else:
        return file_data


def print_number_str_and_word_in_file():
    file_name = 'task_2.txt'
    file_data = read_file(file_name=file_name)
    print('\nЗадание 2.')
    if file_data:
        print(f'В файле "{file_name}" {len(file_data)} строк')
        for line in file_data:
            # подсчитываем количество слов через регулярки
            word_number = len(re.findall(r'[a-zA-Zа-яА-Я]* ', line))
            print(f'В {file_data.index(line) + 1} строке {word_number} слов')


def employee_salary():
    """Вывод фамилии сотрудников, у кого оклад меньше 20000 и среднюю ЗП"""
    print('\nЗадание 3')
    file_data = read_file(file_name='task_3.txt')
    employees = [line.split() for line in file_data]
    employees = {line[0]: int(line[1]) for line in employees}
    fond_salary = 0
    print('Сотрудники имеющие оклад менее 20 тыс.:')
    for key, value in employees.items():
        fond_salary += value
        if value < 20000:
            print(key)
    average_salary = fond_salary / len(employees)
    print(f'Средняя ЗП = {average_salary} руб.')


def replace_numerals():
    file_name = 'task_4.txt'
    print(f'\nЗадание 4. В файле {file_name} произойдёт замена')
    # Считываем данные из файла в одну строку
    with open(file_name, 'r', encoding='utf-8') as file:
        file_data = file.read()
    # Словарь для замены
    dict_numerals = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }
    # Заменяем в числительные в строке
    for key, value in dict_numerals.items():
        file_data = re.sub(key, value, file_data)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(file_data)


def generate_random_sequence_of_numbers():
    """Генерирует немного рандомную последовательность чисел для записи в
    файл"""
    amount_of_numbers = randint(4, 10)
    output_data = ''
    for i in range(amount_of_numbers):
        output_data += str(randint(1, 100)) + ' '
    return output_data


def sum_numbers_in_file():
    print('\nЗадание 5')
    file_name = 'task_5.txt'
    sequence_of_numbers = generate_random_sequence_of_numbers()
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(sequence_of_numbers)
    with open(file_name, 'r', encoding='utf-8') as file:
        numbers = [int(number) for number in file.read().split()]
        print(f'Сумма {numbers} = {sum(numbers)}')


def hours_education():
    print('\nЗадание 6')
    file_name = 'task_6.txt'
    file_data = read_file(file_name)
    academic_subjects = {}
    for line in file_data:
        name = line.split()[0][:-1]
        hours = sum([int(number) for number in re.findall(r'\d+', line)])
        academic_subjects[name] = hours
    print(academic_subjects)


def firm_revenue():
    file_name = 'task_7.txt'
    print(f'\nЗадание 7. Исходный файл {file_name}')
    file_data = read_file(file_name)
    all_profit = 0
    count_profit = 0
    firm_dict = {}
    for line in file_data:
        proceeds = int(line.split()[-1])
        costs = int(line.split()[-2])
        firm_name = ' '.join(line.split()[:-3])
        profit = proceeds - costs
        firm_dict[firm_name] = profit
        if profit > 0:
            all_profit += profit
            count_profit +=1
    profit_dict = {"average_profit": all_profit / count_profit}
    list_data = [firm_dict, profit_dict]
    print(list_data)
    # Насколько правильно использовать такую конструкцию, чтобы была
    # корректная кодировка у файла?
    with open('task_7_1.txt', 'w', encoding='utf-8') as file:
        json.dump(list_data, file, ensure_ascii=False)


if __name__ == '__main__':
    output_in_file()
    print_number_str_and_word_in_file()
    employee_salary()
    replace_numerals()
    sum_numbers_in_file()
    hours_education()
    firm_revenue()
