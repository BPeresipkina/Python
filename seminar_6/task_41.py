'''
Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве.
Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел.

Ввод: 
5
1 2 3 4 5
Вывод:
0
Ввод: 
5
1 5 1 5 1
Вывод:
2

(каждое число вводится с новой строки)
'''

n = int(input('Введите кол-во элементов массива: '))
array = [int(input('Введите число: ')) for i in range(n)]
count = 0

for i in range(1, n-1):
    if array[i] > array[i-1] and array[i] > array[i+1]:
        count += 1
print(count)