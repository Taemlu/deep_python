# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions

first_str = input("Введите первую дробь в виде 'a/b': ")
second_str = input("Введите вторую дробь в виде 'a/b': ")

first_list = first_str.split(sep='/')
second_list = second_str.split(sep='/')

a_1 = int(first_list[0])
a_2 = a_2_2 = int(first_list[1])
b_1 = int(second_list[0])
b_2 = int(second_list[1])
print("Произведение дробей равно: ", a_1 * b_1, "/", a_2 * b_2)

if a_2 != b_2:
    a_1 *= b_2
    a_2 *= b_2
    b_1 *= a_2_2
    b_2 *= a_2_2
    print("Сумма дробей равна: ", a_1 + b_1, "/", a_2)

else:
    print("Cумма дробей равна: ", a_1 + b_1, "/", a_2)

frac_str_1 = fractions.Fraction(a_1, a_2)
frac_str_2 = fractions.Fraction(b_1, b_2)
print("Произведение дробей через fractions равно: ", frac_str_1 * frac_str_2)
print("Cумма дробей через fractions равна: ", frac_str_1 + frac_str_2)
