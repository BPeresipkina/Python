'''
Найти наименьшее общее кратное (НОК) и наибольший общий делитель (НОД)
'''

a = int(input('Введите число: '))
b = int(input('Введите число: '))

for i in range(min(a,b), 1, -1):
    if a % i == 0 and b % i == 0:
        nod = i
        break
for i in range(max(a,b), a*b):
    if i % a == 0 and i % b == 0:
        nok = i
        break

print(f'НОК = {nok}')
print(f'НОД = {nod}')