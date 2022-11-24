#Управляющая конструкции
#elif - встроенная проверка 
#while 
#for i in enumeration:

original = 23
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //=10
    print(original)
else:
    print('Пожалуй, хватит')
print(inverted)

#for i in range(1, 10, 2): #2 здесь приращение
# for i in 'qwe'
list = [1,2,3,4]
for i in list: 
    print(i)
