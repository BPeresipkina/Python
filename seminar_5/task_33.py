'''
Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: 
все максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

points = [int(input('Введите оценку: ')) for i in range(int(input('Введите кол-во оценок: ')))]
print(points)

max = points[0]
index_max = []
for i in range(len(points)):
    if points[i] == max:
        index_max.append(i)
    elif points[i] > max:
        max = points[i]
        index_max = []
        index_max.append(i)
print(index_max)

for i in index_max:
    points[i] = 1
print(points)    