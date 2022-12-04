# Напишите функцию convert_to_miles(km), которая принимает
# в качестве аргумента расстояние в километрах и возвращает расстояние в милях.
# Формула для преобразования: мили = километры * 0.6214.

# # объявление функции
# def convert_to_miles(km):
#     return km * 0.6214
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))


# Напишите функцию get_days(month),
# которая принимает в качестве аргумента номер месяца
# и возвращает количество дней в данном месяце.

# # объявление функции
# def get_days(month):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     if month in [4, 6, 9, 11]:
#         return 30
#     else:
#         return 28
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))


# Напишите функцию get_factors(num),
# принимающую в качестве аргумента натуральное число и
# возвращающую список всех делителей данного числа.

# # объявление функции
# def get_factors(num):
#     delitel = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             delitel.append(i)
#     return delitel
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))


# Напишите функцию number_of_factors(num),
# принимающую в качестве аргумента число и
# возвращающую количество делителей данного числа.

# объявление функции
def number_of_factors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))