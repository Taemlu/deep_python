# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

a = int(input("Введите целое число: "))
result = ""
b = hex(a)
hex_symbols = '0123456789abcde'
while a > 0:
    result = hex_symbols[a % 16] + result
    a //= 16
print(b, result)
if result == b[2:]:
    print(True)
print(type(result))
print(type(b))
