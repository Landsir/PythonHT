print ('Hello, world')
a = 123
b = 1.23
s = 'hello world'
# print (a)
# print (b)
# s = 'hello, \n world' вывод строки с переносом на другую строку
# print (type (b))
# print (s) #вывод строки 
print (a, b, s)  #вывод строки в ряд
print ('{1} - {2} - {0}' .format(a, b, s))
print(a, '-', b, '-', s)
print(f'{a} - {b} - {s}')

# f = False
# print(f)

list = [1,2,3] #это не массив, поэтому можно любые типы данных, но не надо
print (list) 

#print ('Введите c')
#c = int(input()) #для того,чтобы сложить, нужно объвить тип данных, для вещественых тип float
#print ('Введите d')
#d = int(input())
#print (c, '+' , d, '=', c+d)
# арифмитические операции
# +, -, *, /, %, // (целые числа), ** (возведение в степень)
f = 1.36543764
d = 3
e = round (f * d, 1) #округление
print(e)
