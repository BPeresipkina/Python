'''
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''

min = int(input('Введите нижнюю границу диапазона: '))
max = int(input('Введите верхнюю границу диапазона: '))
array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def index_d(array, min, max):
    massive = list()
    for i in range(len(array)):
        if array[i] <= max and array[i] >= min:
            massive.append(i)
    return massive

print(index_d(array, min, max))