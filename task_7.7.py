# На обработку поступает последовательность из 1010 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10^6
# Нужно написать программу, которая выводит на экран количество неотрицательных
# чисел последовательности и их произведение. Если неотрицательных чисел нет,
# требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4).
# Известно, что каждая ошибка затрагивает только одну строку и может
# быть исправлена без изменения других строк.

# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# На обработку поступает последовательность из 10 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10^6.
# Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел
# последовательности и максимальное отрицательное число в последовательности.
# Если отрицательных чисел нет, требуется вывести на экран «NO».
# Программист торопился и написал программу неправильно.
#
# Найдите все ошибки в этой программе (их ровно 5).
# Известно, что каждая ошибка затрагивает только одну
# строку и может быть исправлена без изменения других строк.

mx = -(10 ** 6)
s = 0
for i in range(1, 11):
    x = int(input())
    if x < 0:
        s = s + x
    if 0 > x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print("NO")
