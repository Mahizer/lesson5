# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('sum_of_numbers.txt', 'w+', encoding='UTF-8') as numbers:
    numbers.writelines('1 23 346 3 55')
    numbers.seek(0)
    txt = numbers.read()
    count = 0
    for line in txt.split():
        count += int(line)

print(count)
