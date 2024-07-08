import re

def normalize_phone(phone_number):
    # cleanup number, leave only digits and +
    unified_number = re.sub(r'[^\d+]', '', phone_number)
    
    # if starts w/ 0, add +38
    if unified_number.startswith('0'):
        unified_number = '+38' + unified_number
    
    # if starts with 380, add +
    elif unified_number.startswith('380'):
        unified_number = '+' + unified_number
    
    # if not starts with +, add +38
    elif not unified_number.startswith('+'):
        unified_number = '+38' + unified_number
    
    return unified_number

# execute with example from task
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

sanitized_numbers = [normalize_phone(number) for number in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)