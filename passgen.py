import os # для os.startfile
print ("Generated passwords:")
from random import randint # подключаем модуль с функцией рандома
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
f = open('passwords.txt', 'w' )
for j in range(10):
    i = randint(0,23) # Заглавная
    print (a[i], end="")
    f.write(a[i])
    i = randint(0,23) # малая
    print (b[i], end="")
    f.write(b[i])    
    i = randint(0,23) # малая
    print (b[i], end="")
    f.write(b[i])       
    i = randint(2,9) # цифра от 2 до 9 включительно
    print (i, end="")
    f.write(str(i))       
    i = randint(2,9) # цифра от 2 до 9 включительно
    print (i, end="")
    f.write(str(i))      
    i = randint(2,9) # цифра от 2 до 9 включительно
    print (i, end="")
    f.write(str(i))  
    i = randint(0,23) # малая
    print (b[i])
    f.write(b[i])
    f.write('\n')
f.close()
os.startfile('passwords.txt') # открываем сделанное в блокноте
