import re

def normalize_phone(phone_number):

    # Видаляємо всі символи, крім цифр і '+'
    sanitized_number = re.sub(r"[^\d+]", "", phone_number)
    
    # Якщо номер не починається з '+', додаємо код країни
    if not sanitized_number.startswith('+'):
        # Якщо номер починається з '380', просто додаємо '+'
        if sanitized_number.startswith('380'):
            sanitized_number = '+' + sanitized_number
        # В іншому випадку додаємо '+38'
        else:
            sanitized_number = '+38' + sanitized_number
            
    return sanitized_number

# Приклади використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)