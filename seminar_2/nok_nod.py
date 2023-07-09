'''
Найти наименьшее общее кратное (НОК) и наибольший общий делитель (НОД)
'''

a = int(input('Введите число: '))
b = int(input('Введите число: '))

flag = False
for i in range(2, min(a,b)):
    if a % i == 0 and b % i == 0:
        nod = i
        if flag:
            continue
        else:
            nok = i
            flag = True

print(f'НОК = {nok}')
print(f'НОД = {nod}')