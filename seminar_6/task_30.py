'''
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an  = a1  + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''

a = int(input('Введите первое число: '))
n = int(input('Введите кол-во элементов в последовательности: '))
d = int(input('Введите шаг в последовательности: '))

def massive_ap(a, n, d):
    array = [a] * n
    for i in range(1, n):
        array[i] = array[i-1] + d
    return array

print(massive_ap(a, n, d))