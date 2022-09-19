"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main():
    age = int(input(f'enter a number: '))
    if age < 5:
        print(f'user is {age} years old. user attends kindergarten')
    elif age < 15:
        print(f'user is {age} years old. user attends school')
    elif age < 20:
        print(f'user is {age} years old. user visits institute')
    elif age > 20:
        print(f'user is {age} years old. user works')


if __name__ == "__main__":
    main()
