#Перше завдання

from datetime import datetime, timedelta

def get_days_from_today(date):

    specific_date = datetime(year=2020, month=4, day=21).date()                    #створення об'єкта datetime з певною датою
    print(specific_date, " - створення об'єкта datetime з певною датою")           #для себе перевіряю яку дату показує

    current_date = datetime.today().date()                                         #отримання поточної дати
    print(current_date, " - отримання поточної дати")                              #для себе перевіряю яку дату показує
    
    different_days = (current_date - specific_date).days                           #знаходимо різницю між двома датами
    print("Різниця між датами, число: ", different_days)                           #вивести різницю (число) між датами
    print("Тип надрукованого числа: ", type(different_days))                       #для себе перевіряю який тип надрукованого числа показує


get_days_from_today(date="")                                                       #виклик функції

#Результат:
# 2020-04-21  - створення об'єкта datetime з певною датою
# 2024-04-21  - отримання поточної дати
# Різниця між датами, число:  1461
# Тип надрукованого числа:  <class 'int'>


