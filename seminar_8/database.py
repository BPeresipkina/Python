from view import *

def write_name(name):
    with open('telephone.txt', 'a', encoding='utf-8') as file:
        file.write(name)

def search_data(char):
    with open('telephone.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        count = 1
        for row in lst:
            if char in row:
                print(f'{count} строка {row}') # сделать, чтобы выводилось: (1, row такая-то)/(2, row такая-то)
            count += 1
            
def change_data(id):
    with open('telephone.txt', 'r+', encoding='utf-8') as file:
        lst = file.readlines()
        with open('telephone.txt', 'w', encoding='utf-8') as file:
            file.write('')
            file.close
        for row in lst:
            if id != row.split(',')[0]:
                write_name(row)
            else:
                write_name(input_name())
                # n = int(input('Какую характеристику хотите изменить:\n1 - id\n2 - Имя\n3 - Телефон\n'))
                # for i in (len(row.split(','))):
                #     if i == n-1:

def delete_data(id):
    with open('telephone.txt', 'r+', encoding='utf-8') as file:
        lst = file.readlines()
        with open('telephone.txt', 'w', encoding='utf-8') as file:
            file.write('')
            file.close
        for row in lst:
            if id != row.split(',')[0]:
                write_name(row)