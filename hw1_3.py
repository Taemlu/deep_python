# Напишите код,
# который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
my_number = int(input("Введите число от 2 до 100 000: "))
MIN_NUMBER = 2
MAX_NUMBER = 100000

while my_number < MIN_NUMBER or my_number > MAX_NUMBER:
    my_number = int(input("Введите число от 2 до 100 000: "))
check_number = 2
flag = 'простое'

if check_number < my_number:
    if (my_number % check_number) == 0:
        flag = 'составное'
    else:
        check_number += 1

print(f'число {my_number} - {flag}')
