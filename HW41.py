# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random as r
from sympy import poly
from sympy.abc import x
number = int(input("Введите N"))
some_str = ''
while number>=0:
    a = r.randint(1, 100)
    some_str += str(a*(x)**number) + "+"
    number -=1
b = r.randint(1, 100)
print(some_str[:-1]+ ' = 0')