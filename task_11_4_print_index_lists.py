# Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# summa = 0
# for i in numbers:
#     multi = i ** 2
#     summa += multi
# print(summa)


# На вход программе подается натуральное число nn, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x
# выводит значение функции f(x) = x^2 + 2x + 1, каждое на отдельной строке.


# n = int(input())
# l1 = []
# l2 = []
# for i in range(n):
#     l1.append(int(input()))
# for i in l1:
#     l2.append(i ** 2 + 2 * i + 1)
# print(*l1, sep='\n')
# print()
# print(*l2, sep='\n')


# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
#
# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

# n = int(input())
# l1 = []
# for i in range(n):
#     l1.append(int(input()))
# for j in l1:
#     if j != min(l1) and j != max(l1):
#         print(j)


# На вход программе подается натуральное число nn, а затем nn строк.
# Напишите программу, которая выводит только уникальные строки,
# в том же порядке, в котором они были введены.

# n = int(input())
# l1 = []
# for i in range(n):
#      s = input()
#      if s not in l1:
#          l1.append(s)
# print(*l1, sep='\n')


# На вход программе подается натуральное число n,
# затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки,
# в которых встречается поисковый запрос.

# n = int(input())
#
# l1 = []
# for i in range(n):
#     l1.append(input())
# k = input()
# for j in range(len(l1)):
#     if k.lower() in l1[j].lower():
#         print(l1[j])


# На вход программе подается натуральное число n, затем n строк,
# затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки,
# в которых встречаются все поисковые запросы.

# s = []  # обьявляем основной список
# p = []  # обьявляем поисковый список
#
# for _ in range(int(input())):  # количество элементов основного списка
#     s.append(input())  # добавляем элементы
#
# for _ in range(int(input())):  # количество элементов поискового списка
#     p.append(input())  # добавляем элементы
#
# for i in s:  # Ищем для каждого элемента основного списка
#     n = 0  # счётчик совпадений
#     for k in p:  # сравниваем наличией элемента из списка поиска с основным
#         if k.lower() in i.lower():  # если совпадение найдено:
#             n += 1  # счётчик прибавляет значение
#     if n >= len(
#             p):  # если счётчик совпадений равен или больше количеству элементов поискового списка, печатаем элемент из основного списка.
#         print(i)


# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая сначала выводит все отрицательные числа, затем нули,
# а затем все положительные числа, каждое на отдельной строке.
# Числа должны быть выведены в том же порядке, в котором они были введены.

n = int(input())
l1 = []
lmin = []
l_0 = []
l_plus = []
total = []
for _ in range(n):
    l1.append(int(input()))
for i in l1:
    if i < 0:
        lmin.append(i)
    elif i == 0:
        l_0.append(i)
    else:
        l_plus.append(i)
total.extend(lmin), total.extend(l_0), total.extend(l_plus)
print(*total, sep='\n')




