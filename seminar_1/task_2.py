"""
Найдите сумму цифр трехзначного числа.

Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

n = int(input('Введите число: '))
result = 0
while n>0:  
    result += n % 10
    n = int(n/10)


print(result)

# a = input('Введите число: ')
# result = 0
# for i in a:
#     result += int(i)

# print(result)