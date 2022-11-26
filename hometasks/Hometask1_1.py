# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Input a number of a week day '))
if day > 8:
    print('incorrect number')
elif day == 6 or 7:
    print("yes, it's a holiday, let's have a drink")
else: print("no, this is a working day, work harder")

