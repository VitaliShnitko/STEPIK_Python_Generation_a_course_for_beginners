# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» (без кавычек).
# Напишите программу, которая выводит члены данной последовательности.

# text = input()
# while text != 'КОНЕЦ':
#     print(text)
#     text = input()


# На вход программе подается последовательность слов,
# каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» или «конец»
# (большими или маленькими буквами, без кавычек). Напишите программу,
# которая выводит члены данной последовательности.

# text = input()
# while text != 'КОНЕЦ' and text != 'конец':
#     print(text)
#     text = input()


# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является одно из трех слов: «стоп», «хватит»,
# «достаточно» (маленькими буквами, без кавычек).
# Напишите программу, которая выводит общее количество членов данной последовательности.

# text = input()
# count = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     count += 1
#     text = input()
# print(count)

# На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке.
# Концом последовательности является любое число не делящееся на 7.
# Напишите программу, которая выводит члены данной последовательности.


# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())


# На вход программе подается последовательность целых чисел, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число.
# Напишите программу, которая выводит сумму всех членов данной последовательности.


# num = int(input())
# total = 0
# while num > -1:
#     total += num
#     num = int(input())
# print(total)


# На вход программе подается последовательность целых чисел от 11 до 55, характеризующее оценку ученика,
# каждое число на отдельной строке. Концом последовательности является любое отрицательное число,
# либо число большее 55. Напишите программу, которая выводит количество пятерок.


num = 1
count = 0
while 1 <= num <= 5:
    num = int(input())
    if num == 5:
        count += 1
print(count)







