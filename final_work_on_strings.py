# Вставьте пропущенный фрагмент кода,
# так чтобы в результате выполнения программы была выведена длина строки s.

# s = 'Python rocks!'
# print(len(s))


# Вставьте пропущенный фрагмент кода,
# так чтобы в результате выполнения программы был выведен четвертый символ строки s.

# s = 'Python rocks!'
# print(s[3])


# Вставьте пропущенный фрагмент кода,
# так чтобы в результате выполнения программы
# были выведены символы строки s со 2 по 5 включительно.

# s = 'Python rocks!'
# print(s[1:5])


# Вставьте пропущенный фрагмент кода,
# так чтобы в результате выполнения программы была
# выведена строка s без ведущих и замыкающих пробельных символов.

# s = '    Python rocks!     '
# print(s.strip())


# Вставьте пропущенный фрагмент кода,
# так чтобы в результате выполнения программы
# была выведена строка s заглавными буквами (в верхнем регистре).

# s = 'Python rocks!'
# print(s.upper())


# Вставьте пропущенный фрагмент кода,
# так чтобы в результате выполнения программы
# была выведена строка s в которой символ «o» заменен на символ «@».

# s = 'Python rocks!'
# print(s.replace('o', '@'))


# На вход программе подается строка текста.
# Напишите программу, которая удаляет из нее все
# символы с индексами кратными 3, то есть символы с индексами 0, 3, 6, ....

# text = input()
# a = ''
# for i in range(len(text)):
#     if i % 3 != 0:
#         a += text[i]
# print(a)


# На вход программе подается строка текста.
# Напишите программу, которая заменяет все вхождения цифры 1 на слово «one».

# text = input()
# print(text.replace('1', 'one'))


# На вход программе подается строка текста.
# Напишите программу, которая удаляет все вхождения символа «@».

# text = input()
# print(text.replace('@', ''))


# На вход программе подается строка текста.
# Напишите программу, которая выводит индекс второго вхождения буквы «f».
# Если буква «f» встречается только один раз,
# выведите число -1, а если не встречается ни разу, выведите число -2.

text = input()
if text.count('f') == 1:
    print('-1')
elif text.count('f') >= 2:
    text2 = text.replace('f', '*', 1)
    print(text2.find('f'))
else:
    print('-2')