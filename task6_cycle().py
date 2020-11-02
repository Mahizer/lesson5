from itertools import cycle

my_list = ('зима', 'весна', 'лето', 'осень')

count = 0

for el in cycle(my_list):
    if count > 15:
        break
    print(el)
    count += 1
