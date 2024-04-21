#Друге завдання
from random import randint

result_values = set()

def get_numbers_ticket(min_value, max_value, quantity):
    while len(result_values) != quantity:
        result_values.add(randint(min_value, max_value))
    print("Ваші лотерейні числа:", sorted(list(result_values)))

get_numbers_ticket(1, 49, 6)