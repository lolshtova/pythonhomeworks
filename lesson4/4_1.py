from sys import argv


def zarabotok(time, paid_fot_time, bonus):
    z = int(time) * int(paid_fot_time) + int(bonus)
    return z


_, time, paid_for_time, bonus = argv
print('зарплата всего', zarabotok(time, paid_for_time, bonus))
