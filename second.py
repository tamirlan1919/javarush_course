import random


def get_number():
    x = random.randint(1, 10)
    number = int(input('Введите число: '))
    while True:
        if x == number:
            print('В точку')
            break
        else:
            print('Промах')