# Геометрической прогрессией называется последовательность чисел b_1, b_2,...., b_n , каждое из которых, начиная с b_2 ,
# получается из предыдущего умножением на одно и то же постоянное число qq (знаменатель прогрессии), то есть
#
# b_n=b_{n−1}* q
#
# Если известен первый член прогрессии и её знаменатель, то n-ый член геометрической прогрессии находится по формуле
#
# b_n=b_1* q^{n-1}


# b_1 = int(input())
# q = int(input())
# n = int(input())
#
# b_n = b_1 * (q**(n-1))
#
# print(b_n)

# Напишите программу, которая находит полное число метров по заданному числу сантиметров.

# amount_sm = int(input())
# count_met = amount_sm // 100
# print(count_met)

# n школьников делят k мандаринов поровну,
# неделящийся остаток остается в корзине.
# Сколько целых мандаринов достанется каждому школьнику?
# Сколько целых мандаринов останется в корзине?

# amount_schoolboy = int(input())
# amount_mandarin = int(input())
#
# count_mandarin = amount_mandarin // amount_schoolboy
# remainder_mandarin = amount_mandarin % amount_schoolboy
# print(count_mandarin)
# print(remainder_mandarin)

# Безумный титан Танос собрал все 6 камней бесконечности и
# намеревается уничтожить половину населения Вселенной по щелчку пальцев.
# При этом если население Вселенной является нечетным числом,
# то титан проявит милосердие и округлит количество выживших в большую сторону.
# Помогите Мстителям подсчитать количество выживших.

# n_people = int(input()) + 1
# r_people = n_people // 2
# print(r_people)

# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
# Напишите программу, которая определяет номер купе,
# в котором находится место с заданным номером.

# num_place = int(input())
# places = num_place + 3
# kupe = int(places / 4)
# print(kupe)

# Напишите программу для пересчёта величины временного интервала,
# заданного в минутах, в величину, выраженную в часах и минутах.

# minuts = int(input())
# hour = minuts // 60
# minut = minuts % 60
# print(minuts, 'мин', '-', 'это', hour, 'час', minut, 'минут.')

# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

# digit = int(input())
# digit1 = digit // 100
# digit2 = (digit // 10) % 10
# digit3 = digit % 10
# sum_digit = digit1 + digit2 + digit3
# multi_digit = digit1 * digit2 * digit3
# print('Сумма цифр =', sum_digit)
# print('Произведение цифр =', multi_digit)


# Дано трехзначное число abc,
# в котором все цифры различны. Напишите программу, которая выводит шесть чисел,
# образованных при перестановке цифр заданного числа.

digit = int(input())
digit1 = digit // 100
digit2 = (digit // 10) % 10
digit3 = digit % 10
print(digit)
print(digit1 * 100 + digit3 * 10 + digit2)
print(digit2 * 100 + digit1 * 10 + digit3)
print(digit2 * 100 + digit3 * 10 + digit1)
print(digit3 * 100 + digit1 * 10 + digit2)
print(digit3 * 100 + digit2 * 10 + digit1)
















