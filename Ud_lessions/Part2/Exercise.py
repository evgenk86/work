# Exercise 1

# напишите выражение внутри print(...) в результате которого
# на консоль должно выводиться число 12

from cmath import pi


print(5+7)

# Exercise 2
# Объявите переменную name и присвойте ей значение 'John Snow', и переменную с именем age и присвойте ей значение 29
name = 'John Snow'
age = 29

# Exercise 3
# Измените код так, чтобы он соответствовал тексту в комментариях.

print("I'm a student and I'll become a \"strong\" programmer") #I'm a student and I'll become a "strong" programmer

# можно также в 3 """ или '''
print("""I'm a student and I'll become a "strong" programmer""")

print(r"C:\Users\GoodStudent") #C:\Users\GoodStudent

x = "My name is Agent Smith"
print(x[1]) #y - 1 т.к. первый символ это 0
print(x[3:18:3]) #nesgt срез начиная с 3го символа в следующих 18ти символах вывести каждый 3й символ

# Exercise 4
# 1. Клиент покупает кофе в кафе. За каждые 6 чашек, 1 чашка даётся в качестве бонуса.
# Задача: запросить у пользователя кол-во чашек на покупку, вычислить полагающееся кол-во бонусных чашек кофе и вывести это число на консоль

cof = input('Введите количество чашек кофе: ')
cups = int(cof)
free_cups = int(cups / 6) # чтобы не получилось дробное число передаем в int
print(free_cups)

# более упрощенный вид

# cups = int(input('Введите количество чашек кофе: '))
# print(int(cups / 6))

# Exercise 5
# 2. Запросить у пользователя координаты x и y двух точек на плоскости. 
# Посчитать расстояние между заданными точками и вывести результат на консоль с точностью до трёх знаков после запятой (плавающей точки).

# Примечание: у каждой точки есть две координаты: x и y. 
# Расстояние рассчитывается по формуле, которую вы с лёгкостью найдёте в Интернете (да, гуглить всё, что вы не знаете - очень полезно!).

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

distance = round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 3)
#distance = round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 3)

print(distance)


# Exercise 6

# 3. На ферме есть куры, коровы и свиньи. У курицы две ноги, у свиньи - четыре, у коровы - четыре. 
# Запросить у пользователя (фермера) ввод кол-ва кур, свиней и коров, просуммировать кол-во ног всех животных и вывести результат на консоль.

chicken = int(input('Введите кол-во кур: '))
cows = int(input('Введите кол-во коров: '))
pigs = int(input('Введите кол-во свиней: '))

total_legs = chicken * 2 + (cows + pigs) * 4
print(total_legs)

