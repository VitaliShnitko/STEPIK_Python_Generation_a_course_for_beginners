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

n = int(input())
total = 1

for i in range(1, n+1):
    total *= i
print(total)