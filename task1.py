# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script_name, hours_argv, rate_per_hour_argv, prize_argv = argv


def salary(hours, rate_per_hour, prize):
    return int(hours) * int(rate_per_hour) + int(prize)


print(salary(hours_argv, rate_per_hour_argv, prize_argv))



