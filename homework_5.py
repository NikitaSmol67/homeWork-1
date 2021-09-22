# Exercise 1
my_file = open('test.txt', 'a+')
line = input('Введите текст \n')
while line:
    my_file.writelines(line + '\n')
    line = input('Введите текст \n')
    my_file.seek(0,1)
    if not line:
        break
my_file.close()
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
# Exercise 2
my_file = open('text.txt', 'r+')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('text.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
# Exercise 3
with open('text1.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')
# Exercise 4
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text2.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)
with open('text4.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
# Exercise 5
    def summary():
        with open('text5.txt', 'w+') as file:
            line = input('Введите цифры через пробел \n')
            file.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
summary()
# Exercise 6
subj = {}
with open('text6.txt', 'r') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
# Exercise 7
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('text7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')
with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')