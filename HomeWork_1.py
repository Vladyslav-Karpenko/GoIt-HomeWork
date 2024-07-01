import random
import datetime

#! HomeWork_Task#1


def get_days_from_today(date: str) -> str:
    try:
        result = datetime.datetime.today().date(
        ) - datetime.date(int(date[:4]), int(date[5:7]), int(date[-2:]))
    except ValueError:
        return 'Sorry_your_date_is_uncorrect'
    else:
        return f'From your date we have {result.days} days. Bye'


print(get_days_from_today('2020-10-05'))


#! HomeWork_Task#2


def get_numbers_ticket(min: int = 0, max: int = 0, quantity: int = 0) -> list:
    result = set()
    try:
        while len(result) < quantity:
            result.add(random.randint(min, max))
    except TypeError:
        return f'Something wrong, try again'
    return sorted(list(result))


tickets_result = get_numbers_ticket(1, 49, 6)
print(f'Ваші лотирейні числа: {tickets_result}')
