"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X

5
1 2 3 4 5
6
-> 5
"""

n = int(input('Введи кол-во элементов в массиве: '))
a = [0] * n
x = int(input('Введите число: '))
dif = x
result = x

for i in range(n):
    a[i] = i+1
    if x - a[i] < 0:
        if dif > (x - a[i]) * -1:
            dif = x - a[i]
            result = a[i]
    else:
        if dif > x - a[i]:
            dif = x - a[i]
            result = a[i]
    

print(result)

# # решение преподавателя

# n = int(input())
# lst = [int(input()) for i in range(n)]
# x = int(input())
# min_range = abs(x-lst[0])
# el = lst[0]
# for i in lst:
#     if abs(x-i)< min_range:
#         min_range = abs(x-i)
#         el = i
# print(el)