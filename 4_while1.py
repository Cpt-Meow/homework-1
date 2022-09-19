"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    while True:
        num1 = input(f'Введите что-то: ')
        if num1 == 'Хорошо':
            print(f'exit')
            break
        else:
            print('Как дела?')


if __name__ == "__main__":
    hello_user()
