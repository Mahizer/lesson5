# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('salaries.txt', encoding='UTF-8') as salaries:
    all_s = 0
    line_count = 0
    for line in salaries:
        my_list = line.split()
        my_list[1] = int(my_list[1])
        line_count += 1
        if my_list[1] < 20000:
            print(my_list[0])
            all_s += my_list[1]
        else:
            all_s += my_list[1]
print(f'Средняя величина дохода сотрудников: {all_s / line_count} р.')


