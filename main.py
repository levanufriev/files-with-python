from datetime import timedelta, date
import random
import string

#Generating date.
def generate_date():
    end_date = date.today()
    start_date = date(end_date.year - 5, end_date.month, end_date.day)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime('%d.%m.%Y')

#Generating latin symbols.
def generate_latin():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

#Generating cyrillic symbols.
def generate_cyrillic():
    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return ''.join(random.choice(letters) for _ in range(10))

#Generating integer.
def generate_int():
    return str(random.randrange(2, 100000000, 2))

#Generating float.
def generate_float():
    random_float = random.uniform(1, 20)
    formatted_float = "{:.8f}".format(random_float)
    return str(formatted_float)

#Generating text.
def generate_text(f):
    for _ in range(100000):
        f.write(generate_date()+"||"+generate_latin()+"||"+generate_cyrillic()
                +"||"+generate_int()+"||"+generate_float()+"||\n")


#Generating files.
for i in range(100):
    with open(f'file{i+1}.txt', 'w') as file:
        generate_text(file)
