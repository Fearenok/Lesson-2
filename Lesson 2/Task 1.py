# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

float_num = input('input float number: ')
print(type(float_num))

sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)
print(sum)