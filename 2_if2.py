import re
"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main():
    line_1 = str(input(f'Введите текст 1: '))
    line_2 = str(input(f'Введите текст 2: '))
    print(isinstance(line_1, str), isinstance(line_2, str), sep='\n')
    if line_1 == line_2:
        return 1
    elif (line_1 != line_2) and (len(line_1) > len(line_2)):
        return 2
    elif (line_1 != line_2) and (line_2.find('learn')):  # return 3
        return 3
    elif (line_1 != line_2) and (re.search(r'\blearn\b', line_2)):  # return 3(alternative)
        return 4


if __name__ == "__main__":
    main()
