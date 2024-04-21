#Друге завдання
from random import randint                                       #Імпортуємо модуль для генерації випадкових чисел

result_values = set()                                            #Створюємо множину, яка має назву result_values

def get_numbers_ticket(min_value, max_value, quantity):          #Створюємо функцію
    while len(result_values) != quantity:                        #Створюємо цикл для генерації чисел поки лічильник не перевищіть число 6 (бо 6 чисел нам потрібно, не більше)
        result_values.add(randint(min_value, max_value))         #Додаємо рандомно числа від 1 до 49
    print("Ваші лотерейні числа:", sorted(list(result_values)))  #Друкуємо відсортований список

get_numbers_ticket(1, 49, 6)                                     #Викливаємо функцію з параметрами

#Результат:
# Ваші лотерейні числа: [6, 15, 31, 35, 37, 39]