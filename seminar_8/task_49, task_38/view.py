def input_num():
    ask = int(input('Выберите действие:\n1 - Записать новый контакт\n2 - Найти контакт\n3 - Сортировка\n4 - Вывести весь справочник\n'))
    return ask

def input_name():
    print()
    id = input('Введите id контакта: ')
    name = input('Введите имя контакта: ')
    tel = input('Введите телефон контакта: ')
    res = f'{id},{name},{tel}\n'
    return res

def input_chara():
    print()
    char = input('Введите характеристику: ')
    return char

def sort_id(a):
    a.sort(key = lambda x : int(x.split(',')[0]))
    return a
