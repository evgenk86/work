# Кортежи - tuple
# не изменяемый список (лист)

strings = ('str1', 'str2', 'str3')
# strings [0] = 'srt0'

# Выдаст ошибку - TypeError: 'tuple' object does not support item assignment
# Оператор присваивания не поддерживается кортежами 

# tuple - набор связанных данных

person = ('John', 'Silver', 22)

# зачастую tuple содержит значения (данные), которые объеденены каким либо смыслом, н-р как в данном примере Имя, Фамилия и возраст

print(type(person))             # возвращает список типа <class 'tuple'>

# хотя все те же данные можно вести как список

person_info = ['John', 'Silver', 22]
print(type(person_info))       # возвращает список типа <class 'list'>

# но в списке данные могут меняться, а семантика неизменяемости подчёркивает, то что данные в кортежах могут быть связаны друг с другом 
# чаще всего они используются для того чтобы защитить данные от преднамеренного или не преднамеренного изменения

# для определения кол-ва элементов в кортеже используется - 'len'

print(len(person))

# для вывода определенных значений кортежа 

print(person[0])            # для вывода 1го элемента
print(person[-1])           # для вывода последнего элемента

# в списке мы можем переназначить имя

person_info[0] = 'Bob'
print(person_info)

# с кортежем tuple это не сработает

    # person[0] = 'Bob'

# Выдаст ошибку - TypeError: 'tuple' object does not support item assignment
# Оператор присваивания не поддерживается кортежами 

# Кол-во вхождений

print(person.count('John')) # 1 - вхождение

# по какому индексу расположен то или иное значение и возвращает ошибку если элемент не найден

print(person.index('John')) # 0 - стоит на 1м месте 