"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
    while True:
        try:
            num1 = input(f'Введите что-то: ')
            if num1 == 'Хорошо':
                print(f'exit')
                break
            else:
                print('Как дела?')
        except KeyboardInterrupt:
            print('ctrl+c')


if __name__ == "__main__":
    hello_user()
