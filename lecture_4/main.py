list_1 = [1,2,3,5,8,15,23,38]

# a = list()
# for i in list_1:
#     if i % 2 == 0:
#         a.append((i, i**2))
# print(a)

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return[x for x in col if f(x)]

# res = select(int, list_1) # возвращает целые числа
# res = where(lambda x: x%2 == 0, res) # возвращает четные числа
# res = list(select(lambda x: (x, x**2), res)) # возвращает список в виде кортежа (x, x**2)

res = map(int, list_1) # map = select, возвращает целые числа
res = filter(lambda x: x%2 == 0, res) # filter = where, возвращает четные числа
res = list(map(lambda x: (x, x**2), res)) # map = select, возвращает список в виде кортежа (x, x**2)
print(res)