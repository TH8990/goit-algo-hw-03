# Перше завдання.
from datetime import datetime

def get_days_from_today(date_string):
    try:
        # Перетворюємо рядок у об'єкт datetime.date
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()

        # Отримуємо поточну дату.
        today = datetime.today().date()

        # Розраховуємо різницю.
        difference = today - given_date

        # Повертаємо різницю у днях(ціле число).
        return difference.days
    
    except ValueError as e:
        print(f"Помилка: Неправильний формат дати. Очікується 'РРРР-ММ-ДД'. Деталі: {e}")
        return None
    
print(f"Приклад 1: {get_days_from_today('2021-10-10')}")
print(f"Приклад 2 (невірний формат): {get_days_from_today('2023/01/20')}")

