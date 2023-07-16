'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, 
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. 
n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.

11 6

2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12
'''
import random

n = int(input('Введите кол-во элементов первого набора чисел: '))
m = int(input('Введите кол-во элементов второго набора чисел: '))

array_n = []
array_m = []
array_r = set()

for i in range(n):
    array_n.append(int(input('Введите число 1-го набора: ')))
# print(array_n)

for i in range(m):
    array_m.append(int(input('Введите число 2-го набора: ')))
# print(array_m)

# for i in array_m:
#     if i in array_n:
#         array_r.add(i)
# # print(array_r)

array_r = set(array_n).intersection(set(array_m))
# print(array_r)

def quicksort(nums):
   
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)
   
print(quicksort(list(array_r)))