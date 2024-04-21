#Перше завдання

from datetime import datetime, timedelta

def get_days_from_today(date):
    specific_date = datetime(year=2023, month=9, day=28).date()                    #створення об'єкта datetime з певною датою
    current_date = datetime.today().date()                                         #отримання поточної дати
    different_days = (current_date - specific_date).days                           #знаходимо різницю між двома датами
    print("Різниця між датами, число: ", different_days)                           #вивести різницю (число) між датами                         
    return different_days


get_days_from_today(date="")                                                       #виклик функції


