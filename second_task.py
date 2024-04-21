#Друге завдання
from random import sample                                       #Імпортуємо модуль для генерації випадкових чисел

def get_numbers_ticket(min_value, max_value, quantity):
        if max_value > min_value > 0 and max_value <= 1000 and min_value != max_value and 0 < quantity < (max_value - min_value) + 1:

            print(sorted(sample(range(min_value, max_value+1), quantity)))
        else:
              print([])


get_numbers_ticket(10, 15, 6)                                     #Викливаємо функцію з параметрами
