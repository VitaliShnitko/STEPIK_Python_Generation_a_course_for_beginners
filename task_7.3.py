# На вход программе подаются два целых числа a и b (a≤b). Напишите программу,
# которая подсчитывает количество чисел в диапазоне от a до b включительно,
# куб которых оканчивается на 4 или 9.

# a = int(input())
# b = int(input())
#
# counter = 0
# for i in range(a, b+1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#         counter += 1
# print(counter)

# На вход программе подается натуральное число n, а затем nn целых чисел,
# каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел.

# n = int(input())
# total = 0
#
# for i in range(n):
#     num = int(input())
#     total += num
# print(total)


# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
# Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.

# from math import log
#
# n = int(input())
# counter = 0
# for i in range(1, n+1):
#     counter = counter + (1 / i)
#     num = counter - log(n)
# print(num)


# На вход программе подается натуральное число nn. Напишите программу,
# которая подсчитывает сумму тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2,5 или 8.

# n = int(input())
# total = 0
# for i in range(1, n+1):
#     if (i**2) % 10 == 2 or (i**2) % 10 == 5 or (i**2) % 10 == 10:
#         total += i
# print(total)

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.

# n = int(input())
# total = 1
#
# for i in range(1, n+1):
#     total *= i
# print(total)

# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

# total = 1
#
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)


# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет сумму всех его делителей.

# n = int(input())
# total = 0
#
# for i in range(1, n+1):
#     if n % i == 0:
#         total += i
# print(total)


# На вход программе подается натуральное число n.
# Напишите программу вычисления знакочередующей суммы.

# n = int(input())
# total = 0
#
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
# print(total)


# На вход программе подается натуральное число n, а затем n различных натуральных чисел,
# каждое на отдельной строке. Напишите программу,
# которая выводит наибольшее и второе наибольшее число последовательности.

n = int(input())
max1 = 0
max2 = 1
for i in range(1, n+1):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
print(max1)
print(max2)

