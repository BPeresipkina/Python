'''
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

Input: 2 -> 3 4
Output: 4 3
'''

n = int(input('Введите кол-во элементов последовательности: '))

def revolution(n):
    m = int(input('Введите число: '))
    if n == 1:
        return m
    return revolution(n-1), m

print(revolution(n))

# Решение преподавателя 1:

# def foo(n):
#     if n == 0:
#         return
#     k = input()
#     foo(n-1)
#     print(k)

# n = 3
# foo(n)

# Решение преподавателя 2:

# def foo(n):
#     k = input()
#     if n == 0:
#         return k
#     return foo(n-1) + k

# n = 3
# print(foo(n))