"""
Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. 
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 

Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50

Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""
from random import randint
n = int(input('Введите кол-во дней: '))
# massive = [0] * (n)
# for i in range(n):
#     massive[i] += int(input(f'Введите температуру {i+1} дня: '))

# # print(massive)

# count = 0
# result = 0
# for i in range(n):
#     if massive[i] > 0:
#         count += 1
#         if count>result:
#             result = count
#     else:
#         count = 0

# print(result)

cur_plus = 0
max_plus = 0
for i in range(n):
    temp = randint(-40, 40)
    print(temp, end=' ')
    if temp > 0:
        cur_plus += 1
    else:
        if cur_plus > max_plus:
            max_plus = cur_plus
        cur_plus = 0

if cur_plus > max_plus:
    max_plus = cur_plus
cur_plus = 0

print(f'\n{max_plus}')