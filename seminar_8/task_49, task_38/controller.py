from database import *
from view import *

def main():
    while True:
        num = input_num()
        if num == 1:
            res = input_name()
            write_name(res)
            print()
            print('Успешно записано')
            print()
        if num == 2:
            char = input_chara()
            print()
            search_data(char)
            print('Успешно найдена')
            print()
        if num == 3:
            a = open('telephone.txt', 'r', encoding='utf-8')
            print()
            print(sort_id(a.readlines()))
            print()
        if num == 4:
            a = open('telephone.txt', 'r', encoding='utf-8')
            print()
            print(a.readlines())
            print()

main()