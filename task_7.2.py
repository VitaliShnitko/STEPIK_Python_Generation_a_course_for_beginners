# Даны два целых числа m и n ( m ≤ n). Напишите программу,
# которая выводит все числа от m до n включительно.

# m = int(input())
# n = int(input())
#
# for i in range(m, n+1):
#     print(i)

# Даны два целых числа mm и nn. Напишите программу,
# которая выводит все числа от m до n включительно в порядке возрастания, если m < n,
# или в порядке убывания в противном случае.

# m = int(input())
# n = int(input())
#
# if m < n:
#     for i in range(m, n+1):
#         print(i)
# elif m > n:
#     for i in range(m, n-1, -1):
#         print(i)
# else:
#     print(m)

# Даны два целых числа m и n(m > n). Напишите программу,
# которая выводит все нечетные числа от m до n включительно в порядке убывания.

# m = int(input())
# n = int(input())
#
# for i in range(m, n, -2):
#     if m % 2 != 0:
#         print(i)
#     elif m % 2 == 0:
#         print(i-1)

# Даны два натуральных числа m и n (m ≤ n). Напишите программу,
# которая выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий:
#
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.


# m = int(input())
# n = int(input())
#
# for i in range(m, n+1):
#     if i%17 == 0 or i%3 == 0 and i%5 == 0 or i%10 == 9:
#         print(i)
#
# Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.

n = int(input())

for i in range(1, 11):
    print(n, 'x', i, '=', n * i)


