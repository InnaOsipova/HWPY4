# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей 
# . Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"], 
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? 
# Можно ли использовать словарь в этом случае?


def tesaurus (name):
    for i in range(len(name)):
        print (name [i][0])
        k =[]
        for j in range(len(name)-1):
            print(name[j][0])
            print(name[j])
            if name[j][0] == name [i][0]:
                k.append(name[j])
                print(k)
                name.pop(j)
                print (name)
        d = {name[i][0]: k}
        print(d)


            

dictionary = [ 'Анна', 'Алена', 'Игорь', 'Илья']
tesaurus(dictionary)