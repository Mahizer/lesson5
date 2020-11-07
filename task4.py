# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('number.txt', 'r+', encoding='UTF-8') as number:
    number2 = open('number2.txt', 'w', encoding='UTF-8')
    for line in number:
        my_line = line.split()
        if my_line[0] == 'One':
            my_line[0] = 'Один'
            number2.write(' '.join(my_line)+'\n')
        elif my_line[0] == 'Two':
            my_line[0] = 'Два'
            number2.write(' '.join(my_line)+'\n')
        elif my_line[0] == 'Three':
            my_line[0] = 'Три'
            number2.write(' '.join(my_line)+'\n')
        elif my_line[0] == 'Four':
            my_line[0] = 'Четыре'
            number2.write(' '.join(my_line)+'\n')
