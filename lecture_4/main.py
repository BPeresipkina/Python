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

# res = select(int, list_1)
# print(res)
res = map(int, list_1) # map = select
# print(res)

# res = where(lambda x: x%2 == 0, res)
# print(res)
res = filter(lambda x: x%2 == 0, res) # filter = where
# print(res)

# res = list(select(lambda x: (x, x**2), res))
# print(res)
res = list(map(lambda x: (x, x**2), res)) # map = select
print(res)