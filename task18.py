# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в 
# первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых 
# чисел Ai. Последняя строка содержит число X

from random import randint

n = int(input('Введите количество элементов в списке: '))
max = int(input('Введите максимальное число в списке: '))
x = int(input('Введите заданное число: '))
list = []
for i in range(n):
    list.append(randint(1, max))
print(list)
break_out_flag = False
for i in range(max):
    for j in range(n):
        if list[j] == x + i or list[j] == x - i:
            print(f"Самый близкий элемент к числу {x}: {list[j]}")
            break_out_flag = True
            break
    if break_out_flag:
        break

