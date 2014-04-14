import os # for os.startfile
print ("Generated passwords:")
from random import randint # for random
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
f = open('passwords.txt', 'w' )
for j in range(10):
    i = randint(0,23) # Uppercase letter
    print (a[i], end="")
    f.write(a[i])
    i = randint(0,23) # Lowercase letter
    print (b[i], end="")
    f.write(b[i])    
    i = randint(0,23) # Lowercase letter
    print (b[i], end="")
    f.write(b[i])       
    i = randint(2,9) # number 2 to 9 inclusive
    print (i, end="")
    f.write(str(i))       
    i = randint(2,9) # number 2 to 9 inclusive
    print (i, end="")
    f.write(str(i))      
    i = randint(2,9) # number 2 to 9 inclusive
    print (i, end="")
    f.write(str(i))  
    i = randint(0,23) # Lowercase letter
    print (b[i])
    f.write(b[i])
    f.write('\n')
f.close()
os.startfile('passwords.txt') # open in Notepad
