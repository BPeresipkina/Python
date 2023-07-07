'''
Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте.

Input: 
She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

Output: 13

'''
import re

line = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.\nSo if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(line)
# array = re.split('[ .\n]+', line)
# print(array)
# count = set()

# for i in array:
#     count.add(i.upper())

# print(count)
# print(len(count))

print(len(set(re.split('[ .\n]+', line.lower()))))