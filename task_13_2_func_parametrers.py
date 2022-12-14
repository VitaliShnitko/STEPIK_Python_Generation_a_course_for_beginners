# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.

# объявление функции
# def draw_triangle(fill, base):
#     for i in range(base // 2 + 1):
#         for j in range(i + 1):
#             print(fill, end='')
#         print()
#     for i in range(base // 2, 0, -1):
#         for j in range(i, 0, -1):
#             print(fill, end='')
#         print()
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)


# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.


# # объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)


# Напишите функцию print_digit_sum(),
# которая принимает одно целое число num и выводит на печать сумму его цифр.

# объявление функции
def print_digit_sum(num):
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    print(suma)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)