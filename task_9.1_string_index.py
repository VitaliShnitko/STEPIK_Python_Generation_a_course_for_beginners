# Дополните приведенный код, используя индексатор, так чтобы он вывел символ запятой.

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(s[7])


# Дополните приведенный код, используя индексатор, так чтобы он вывел символ w.

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(s[-10])


# На вход программе подается одна строка.
# Напишите программу,
# которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.

# text = input()
# for i in range(0, len(text), 2):
#     print(text[i])


# На вход программе подается одна строка.
# Напишите программу,
# которая выводит в столбик элементы строки в обратном порядке.

# text = input()
# for i in range(1, len(text)+1):
#     print(text[-i])


# На вход программе подаются три строки:
# имя, фамилия и отчество. Напишите программу,
# которая выводит инициалы человека.

family = input()
name = input()
father_name = input()
print(name[0], family[0], father_name[0], sep='')
