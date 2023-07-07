'''
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

a = int(input('Введите число: '))
b = int(input('Введите число: '))

def degree(num_1, num_2, n):
    if num_2 == 1:
        return num_1
    return degree(num_1 * n, num_2 - 1, n)

print(degree(a, b, a))