#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

a = input('input a number ')
b = map(int,str(a))
result = 1
for i in b:
    result *= i
print (result)