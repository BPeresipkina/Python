'''
Напишите программу, которая принимает на вход строку, 
и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
'''

line = 'a a a b c a a d c d d'
array = line.split()

print(array)

for i in range(len(array)-1):
    n = 1
    for j in range(i, len(array)):
        if j == i and j < len(array)-1:
            j += 1
        if array[i] == array[j]:
            array[j] += f'_{n}'
            n += 1
            print(i, j, array[i], array[j])

print(array)