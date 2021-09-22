# Exercise 1
print('Exercise 1')
from sys import argv
name_script, working_out, hours, the_prize = argv
print(name_script)
print((int(working_out)*int(hours))+int(the_prize))
# Exercise 2
print('Exercise 2')
from random import randint
numbers = []
for i in range(20):
    numbers.append(randint(0, 300))
print(numbers)
c = []
for i in range(len(numbers) - 1):
    n = numbers[i]
    i += 1
    m = numbers[i]
    if m > n:
        c.append(m)
print(c)
# Exercise 3
print('Exercise 3')
my_list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 ==0]
print(my_list)
# Exercise 4
print('Exercise 4')
from random import randint
numbers = []
nice_list = []
for i in range(70):
    numbers.append(randint(1, 100))
print(numbers)
for i in numbers:
   if numbers.count(i) == 1:
       nice_list.append(i)
print(nice_list)
# Exercise 5
print('Exercise 5')
def reducer_func(el, l):
    return el * l
numbers = [ i for i in range(100, 1001) if i % 2 == 0]
from functools import reduce
print(reduce(reducer_func, numbers))
# Exercise 6
print('Exercise 6')
from itertools import cycle
x = int(input('Number? '))
for i in range (x,10):
    print(i)
x = list(range(2))
for i, j in enumerate(cycle(x)):
    print(j, end=' ')
    if i > 10:
         break
# Exercise 7
print('Exercise 7')
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        print(fact)
        fact *= num
    return fact
print(factorial(int(input('Number? '))))
