#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import degree
import numpy as np

some_str = ''
number1 = int(input('введите степень первого многочлена : '))
number2 = int(input('введите степень второго многочлена : '))
#print(degree.form_funk(number, some_str)+ ' = 0')

# Запись многочленов в файлы
f = open('text1.txt','w')
f.write(degree.form_funk(number1, some_str))
f.close()
f = open('text2.txt','w')
f.write(degree.form_funk(number2, some_str))
f.close()

# сложение многочленов
with open ("text1.txt", "r") as f1:
    n1 = [x for x in f1.read().split('+')]
    m1=[]
    for i in range(len(n1)):
        m1.append (int(''.join(map(str, n1[i].split('x')[:1]))))
with open ("text2.txt", "r") as f2:
    n2 = [x for x in f2.read().split('+')]
    m2=[]
    for i in range(len(n2)):
        m2.append (int(''.join(map(str, n2[i].split('x')[:1]))))
with open ("text3.txt", "w") as f3:
    f3.write(str(np.poly1d(np.polyadd(m1, m2))))
p = np.poly1d(np.polyadd(m1, m2))
print(p)