# Задание №1
age = 27
name = 'Nikita'
profession = 'millitary officer'
experience = '7 years'
print(age)
print(name)
print(profession)
print(experience)
age = input('Введите возраст ')
name = input('Введите имя ')
profession = input('Введите професссию ')
experience = input('Введите стаж ')
print(age)
print(name)
print(profession)
print(experience)
# Задание №2
n = int(input('Введите секунды для задачи 2 '))
n = n % 86400
m = n % 3600
print('{}:{:02d}:{:02d}'.format(n // 3600, m // 60, m % 60))
# Задание №3
n = int(input('Введите число '))
print(n + (n*10+n) +(n*100+n*10+n))
# Задание №4
number = int(input('Введите число '))
y = 0
while number > 0 :
    x = number % 10
    number = number // 10
    if x > y :
        y = x
print(y)

# Задание №5
plus = int(input('Введите выручку '))
minus = int(input('Введите издержки '))
if plus > minus:
    print('Прибыль - выручка больше издержек')
    rent = plus - minus
    people = int(input('Введите число сотрудников '))
    p = rent // people
    print('Прибыль фирмы на одного сотрудника {}'.format(p))
else: print('Убыток - издержки больше выручки')
# Задание №6
a = int(input())
b = int(input())
day = 0
while a <= b :
    print('{}-й день:{}'.format(day, a))
    a = a * 1.1
    day += 1
