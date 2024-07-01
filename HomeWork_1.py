import random
import datetime
import re
#! HomeWork_Task#1


# def get_days_from_today(date: str) -> str:
#     try:
#         result = datetime.datetime.today().date(
#         ) - datetime.date(int(date[:4]), int(date[5:7]), int(date[-2:]))
#     except ValueError:
#         return 'Sorry_your_date_is_uncorrect'
#     else:
#         return f'From your date we have {result.days} days. Bye'


# print(get_days_from_today('2020-10-05'))


# #! HomeWork_Task#2


# def get_numbers_ticket(min: int = 0, max: int = 0, quantity: int = 0) -> list:
#     result = set()
#     try:
#         while len(result) < quantity:
#             result.add(random.randint(min, max))
#     except TypeError:
#         return f'Something wrong, try again'
#     return sorted(list(result))


# tickets_result = get_numbers_ticket(1, 49, 6)
# print(f'Ваші лотирейні числа: {tickets_result}')


#! HomeWork_Task#3

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]


# def normalize_phone(phone_number):
#     return f'+380{re.sub(r'\D', '', phone_number)[-9:]}'


# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
