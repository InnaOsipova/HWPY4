import random as r
def form_funk (num, some_str):
    if num == 1:
        a = r.randint(0, 100)
        b = r.randint(0, 100)
        if a == 1 and b > 0:
            some_str += 'x+' + str (b)
        if a == 1 and b == 0:
            some_str += 'x' 
        if a == 0:
            some_str += str (b)
        if a > 1:
            some_str += str(a) + 'x+' + str (b)
        if a == 0 and b ==0:
            return some_str
        return some_str
    else:
        a = r.randint(0, 100)
        if a == 1:
            some_str += 'x' + '**' + str(num) + '+' + form_funk(num-1, some_str)
        if a == 0:
            some_str += form_funk(num-1, some_str)
        if a > 1:
            some_str += str(a) + 'x' + '**' + str(num) + '+' + form_funk(num-1, some_str)
        return some_str
