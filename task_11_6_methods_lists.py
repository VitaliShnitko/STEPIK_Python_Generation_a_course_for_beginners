# Дополните приведенный код, чтобы он:
#
# Заменил второй элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print()

# numbers = [8, 9, 10, 11]
#
# numbers[1] = 17  # Заменил второй элемент списка на 17;
# n = [4, 5, 6]
# numbers.extend(n)  # Добавил числа 4, 5 и 6 в конец списка;
# numbers.pop(0)  # Удалил первый элемент списка;
# numbers += numbers  # Удвоил список;
# numbers.insert(3, 25)  # Вставил число 25 по индексу 3;
# print(numbers)  # Вывел список, с помощью функции print()

# На вход программе подается строка текста, содержащая различные натуральные числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

# s = input().split()
# s = [int(i) for i in s] # преобразование списка строк в список чисел
# max_s = s.index(max(s))
# min_s = s.index(min(s))
# s[max_s], s[min_s] = s[min_s], s[max_s]
# print(*s)


# На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

# text = input().lower().split()
# total = text.count('a') + text.count('an') + text.count('the')
# print('Общее количество артиклей:', total)


# Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали,
# и любезно соглашается помочь им в решении их проблем.
# Одной из такой проблем являлся странный компьютерный вирус,
# который проявлялся в виде появления комментариев к программам на терминалах Братства Стали.
# Известно, что программисты Братства никогда не оставляют комментарии к коду,
# и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им.
# Помогите писцу Ибсену удалить все комментарии из программы.


n = input()
for i in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())

# На вход программе подается строка текста, содержащая целые числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая сортирует и выводит данный список
# сначала по возрастанию, а затем по убыванию.

# s = input().split()
# s = [int(i) for i in s]
# s.sort()
# print(*s)
# s.sort(reverse=True)
# print(*s)
