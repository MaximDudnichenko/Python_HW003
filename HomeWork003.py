# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

n = int(input('Введите число: '))
if n < 0:
    n = -n
lst = []
sum = 0
for i in range(0, n + 1):
    lst.append(i)
    if i % 2 != 0:
        sum += lst[i]
print(lst)
print(sum)


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

n = int(input('Введите число: '))
if n < 0:
    n = -n
lst = []
for i in range(0, n + 1):
    lst.append(i)
result = []
for i in range(0, len(lst)//2 + len(lst) % 2):
    result.append(lst[i] * lst[len(lst)-i-1])
print(lst)
print(result)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

value = int(input('Введите количество членов списка: '))
lst = []
for i in range(0, value):
    lst.append(round(random.uniform(0, 100), 2))
print(lst)
max = round(lst[0] - int(lst[0]), 2)
min = round(lst[0] - int(lst[0]), 2)
for i in range(1, len(lst)):
    temp = round(lst[i] - int(lst[i]), 2)
    if max < temp:
        max = temp
    elif min > temp:
        min = temp
result = max - min
print(f'max =  {max} min = {min}')
print(result)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите целое положительное число: '))
bin_number = ''
while number > 0:
    bin_number = str(number % 2) + bin_number
    number //= 2
print(bin_number)



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите целое положительное число: '))
negafibonacci = [None] * (2 * n + 1)
for i in range(0, n + 1):
    if i == 0 or i == 1:
        negafibonacci[n  + i] = i
        negafibonacci[n  - i] = i
    else:
        negafibonacci[n + i] = negafibonacci[n + i -1] + negafibonacci[n + i - 2]
        negafibonacci[n - i] = (- 1) ** (i + 1) * negafibonacci[n + i]
print(negafibonacci)
