'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def calculator(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Ошибка! Делить на ноль нельзя')
print(calculator(int(input('Первое число: ')), int(input('Второе число: '))))
