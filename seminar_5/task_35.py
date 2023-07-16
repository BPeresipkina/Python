'''
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым 
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

Input: 5
Output: yes
'''

n = int(input('Введите число: '))

def simple_number(n):
    flag = False
    for i in range(n, 0, -1):
        print(i, n%i)
        if n%i == 0 and i!=1 and i!=n: 
            flag = True
        print(flag)
    if flag == True:
        return 'No'
    else:
        return 'Yes'

print(simple_number(n))
