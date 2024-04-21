
import re

phone_numbers = ["+38(050)\\123-32-34", "050t3451234", "(O50)888990O", "38050-1I1-2p2-22", "38o50 111 22 11 jer"]

def normalize_phone(phone_numbers):
    for phone in phone_numbers:
        clear_number = re.sub(r'\D', '', phone)
        if not clear_number.startswith('+'):
            if clear_number.startswith('380'):
                clear_number = '+' + clear_number
            else:
                clear_number = '+380' + clear_number
        print(clear_number)

normalize_phone(phone_numbers)