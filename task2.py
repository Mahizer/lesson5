# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text.txt', encoding='UTF-8') as f:
    count_line = 0
    count_words = 0
    for line in f:
        count_line += 1
        for word in line.split():
            count_words += 1
print(count_line)
print(count_words)



