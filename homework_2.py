import random

def get_numbers_ticket(min_num, max_num, quantity):

    # Перевірка вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000) or not (min_num < quantity < max_num):
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))
        
    return sorted(list(numbers))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа (1-49, 6 шт.): {lottery_numbers}")
lottery_numbers_invalid = get_numbers_ticket(1, 5, 6)
print(f"Некоректні параметри: {lottery_numbers_invalid}")