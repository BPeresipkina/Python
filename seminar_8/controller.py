from database import *
from view import *

def main():
    while True:
        num = input_num()
        if num == 1: # Внести
            res = input_name()
            write_name(res)
            print()
            print('Успешно записано')
            print()
        if num == 2: # Найти
            char = input_chara()
            print()
            search_data(char)
            print('Успешно найдена')
            print()
        if num == 3: # Изменить
            id = cont_id()
            change_data(id)
            print()
            print('Успешно изменено')
            print()
        if num == 4: # Удалить
            id = cont_id()
            delete_data(id)
            print()
            print('Успешно удалено')
            print()
        if num == 5: # Вывести справочник
            a = open('telephone.txt', 'r', encoding='utf-8')
            print()
            print(a.readlines())
            print()
        if num == 6: # Отсортировать
            a = open('telephone.txt', 'r', encoding='utf-8')
            print()
            print(sort_id(a.readlines()))
            print()
        
main()