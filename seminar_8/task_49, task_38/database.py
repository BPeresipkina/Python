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
