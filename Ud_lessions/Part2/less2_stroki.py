# Работа со строками

from tkinter.ttk import Separator


x = "hello, my name is John"

# Функция len(x) - подсчитать кол-во символов в строке
print(len(x))

print(x[len(x)-1]) # Взять длинну строки, отнять 1 с конца и вывести это значение

# x.count() # подсчет кол-ва вхождений к-либо символа
print (x.count('l')) # например кол-во 'l' в строке

# функция capitalize - переводит 1ый смвол в верхний регистр. а все остальные (не важно сколько) в нижний.
print(x.capitalize())

# функция upper - переводит всю строку в верхний регистр
print(x.upper())

# можно передать к-либо переменной и делать с ней что хотим, не изменяя значение переменной "х"
upper_cased = x.upper()
print(upper_cased)

# функция lower - переводит всю строку в нижний регистр
print(x.lower())

lower_cased = x.lower()
print(lower_cased)

print(x)

# Функция проверки находятся ли все символы в верхнем "isupper" или нижнем регистрах "islower"

print(upper_cased.isupper()) # Проверка все ли строки находятся в верхнем регистре  / True
print(lower_cased.islower()) # Проверка все ли строки находятся в нижнем регистре   / True
print(x.isupper()) # Проверка что вернут строки в исходном значении "х"             / False
print(x.islower()) # False, т.к. в исходном есть как верхний так и нижний регистры  / False

# Функция find 
print (x.find('l')) # найти где находится символ 'l' (под каким тндексом)- результатом является только 1ый найденный символ
print (x.find('l', 3)) # найти где находится символ 'l', начиная с какого индекса начинать искать н-р:5
print (x.find('l', 3, 10)) # начать с 3 закончить на 10
print (x.find('m', 3, 15)) # начать с 3 закончить на 15

# Результат -1 означает - не найдено 
# также можно искать подстроки
print (x.find('my'))

# Проверка состоит ли строка только из чисел или только букв
print ('123abc'.isalnum()) # в нашем случае вернет значение True
print ('123abc!'.isalnum()) # должен вернуть значение False т.к. строка содержит только цифры и буквы, без символов

print ('123abc'.isalpha()) # в нашем случае вернет значение False, т.к. строка содержит только буквы
print ('abc'.isalpha()) # должен вернуть значение True, т.к. строка содержит только буквы

# проверка строки на пустоту

print ('   '.isspace()) # вернёт True, т.к. строка не пустая
print (''.isspace()) # вернёт False, т.к. строка пустая

# чтобы проверить пустая ли сторочка
empty_string = ""
print(empty_string == "")

# чтобы проверить пустая ли сторочка
empty_string = " "
print(empty_string.strip(" ") == "") # удалит все символы указанные в скобках и дальше проверка на пустоту

# empty_string = ""
# if not empty_string:
#     print('Не пустая')
# else:
#     print('Пустая')

h = "hello"
print(h.startswith('he')) # проверят начинается ли строчка с определенной подстроки
print(h.endswith('lo')) # проверяет заканчивается ли эта строка с данной подстроки

# Функция split разбивает строку на части изспользуя определенный разделитель
split = h.split('l') # разделяя по 'l' получаем ['he', '', 'o']
print(type(split))
print(split)
split = h.split('e') # разделяя по 'l' получаем ['h', 'llo']
print(split)

# Пример
data = '12;10;8;10' # считываем данные
# нужно его разобрать и проанализировать
separated_data = data.split(';')
print(separated_data) # выведет список чисел ['12', '10', '8', '10'] с которыми мы уже в дальнейшем можем работать









