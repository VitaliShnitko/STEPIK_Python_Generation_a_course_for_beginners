# Напишите функцию draw_triangle(),
# которая выводит звездный равнобедренный треугольник
# с основанием и высотой равными 1515 и 88 соответственно:

# # объявление функции
# def draw_triangle():
#     pass
#
# # основная программа
# draw_triangle()  # вызов функции


# Интернет магазин осуществляет экспресс доставку для своих
# товаров по цене 1000 рублей за первый товар и 120 рублей за
# каждый последующий товар. Напишите функцию get_shipping_cost(quantity),
# которая принимает в качестве аргумента натуральное число
# quantity – количество товаров в заказе и возвращает стоимость доставки.

# # объявление функции
# def get_shipping_cost(quantity):
#     total = 1000
#     if quantity == 1:
#         return total
#     else:
#         total = total + ((n-1) * 120)
#         return total
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_shipping_cost(n))


# Магическая дата – это дата, когда день, умноженный на месяц,
# равен числу образованному последними двумя цифрами года.
# Напишите функцию, is_magic(date) которая принимает в качестве
# аргумента строковое представление корректой даты и возвращает
# значение True если дата является магической и False в противном случае.

# # объявление функции
# def is_magic(date):
#     date_lst = date.split('.')
#     return int(date_lst[0]) * int(date_lst[1]) == int(date_lst[2]) % 100
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))


# Напишите функцию compute_binom(n, k),
# которая принимает в качестве аргументов два натуральных
# числа n и k и возвращает значение биномиального коэффициента


# # объявление функции
# import math
# def compute_binom(n, k):
#     total = int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
#     return total
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))


# Напишите функцию get_month(language, number),
# которая принимает на вход два аргумента language – язык ru или en
# и number – номер месяца (от 1 до 12) и возвращает название месяца
# на русском или английском языке.

# объявление функции
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']
    if language == 'ru':
        print(lng_ru[number - 1])
    elif language == 'en':
        print(lng_en[number - 1])

    # считываем данные
lan = input()
num = int(input())

# вызываем функцию
get_month(lan, num)