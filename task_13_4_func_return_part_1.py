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

# # объявление функции
# def number_of_factors(num):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#     return count
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_of_factors(n))


# Напомним, что строковый метод find('a') возвращает
# местоположение первого вхождения символа a в строке.
# Проблема заключается в том, что данный метод не находит местоположение всех символов а.
#
# Напишите функцию с именем find_all(target, symbol),
# которая принимает два аргумента:
# строку target и символ symbol и возвращает список,
# содержащий все местоположения этого символа в строке.

# # объявление функции
# def find_all(target, symbol):
#     l = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             l.append(i)
#     return l
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))


# Напишите функцию merge(list1, list2),
# которая принимает в качестве аргументов два отсортированных по возрастанию списка,
# состоящих из целых чисел, и объединяет их в один отсортированный список.

# # объявление функции
# def merge(list1, list2):
#     l = sorted(list1 + list2)
#     return l
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))


# На вход программе подается число n, а затем n строк,
# содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу,
# которая объединяет указанные списки в один отсортированный
# список с помощью функции quick_merge(), а затем выводит его.

def quick_merge(lst1, lst2):
    res = []
    p1, p2 = 0, 0
    while p1<len(lst1) and p2<len(lst2):
        if lst1[p1] < lst2[p2]:
            res.append(lst1[p1])
            p1+=1
        else:
            res.append(lst2[p2])
            p2+=1
    if p1==len(lst1):
        res += lst2[p2:]
    else:
        res += lst1[p1:]
    return res
res = []
for _ in range(int(input())):
    num = [int(c) for c in input().split()]
    res = quick_merge(res, num)
print(*res)