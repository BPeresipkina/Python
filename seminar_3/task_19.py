"""
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, 
K – положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]

Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""

n = int(input('Введите кол-во чисел в последовательности: '))
array = [0] * n

for i in range(n):
    array[i] = int(input('Введите число: '))

print(array)

k = int(input('Введите число, на которое нужно сдвинуть последовательность: '))
result = [0] * n

for i in range(n):
    if i+k > n-1:
       result[i] = array[i+k-n] 
    else:
        result[i] = array[i+k]

print(result)

# # Доп. решение 1
# for i in range(k):
#     array.insert(0, array.pop())
# print(array)

# # Доп. решение 2
# a1 = array[-k:]
# a2 = array[:-k]
# print(a1 + a2)