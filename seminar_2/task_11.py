"""
Дано натуральное число A > 1. 
Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1.

Input: 5
Output: 6
"""

a = int(input('Введите число: '))

f1 = 0
f2 = f3 = 1

count = 4
result = 0
if a == f1:
    print(1)
elif a == f2:
    print(f'2 или 3')
else:
    while result<a:
        result = f2 + f3
        f2 = f3
        f3 = result
        if a == result:
            print(count)
        count += 1
        
    if result>a:
        print(-1)
