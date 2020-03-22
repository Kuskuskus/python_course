# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
print('__Task1__')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
students_out = dict()
num = 0
for student in students:
  if students_out.get(student['first_name']):
    students_out[student['first_name']] += 1
  else:
    students_out[student['first_name']] = 1
for name, count in students_out.items():
  print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
print('__Task2__')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
students_out = dict()
num = 0
for student in students:
  if students_out.get(student['first_name']):
    students_out[student['first_name']] += 1
  else:
    students_out[student['first_name']] = 1
max_value = max(students_out.values())
for student, num in students_out.items():
  if num == max_value:
    print(f'Самое частое имя среди учеников: {student}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
print('__Task3__')
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
students_out = dict()
num = 0
school_class = 0
for each_class in school_students:
  school_class += 1
  for student in each_class:
    if students_out.get(student['first_name']):
      students_out[student['first_name']] += 1
    else:
      students_out[student['first_name']] = 1
  max_value = max(students_out.values())
  for student, num in students_out.items():
    if num == max_value:
      print(f'Самое частое имя среди учеников {school_class} класса: {student}')
  students_out.clear()

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
print('__Task4__')
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
male_num = 0
female_num = 0
for school_class in school:
  for student in school_class['students']:
    if is_male[student['first_name']] == False:
      female_num += 1
    else:
      male_num += 1
  print(f'В классе {school_class["class"]} {female_num} девочки и {male_num} мальчика')
  female_num = 0
  male_num = 0

# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
print('__Task5__')
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
male_num = 0
female_num = 0
for school_class in school:
  for student in school_class['students']:
    if is_male[student['first_name']] == False:
      female_num += 1
    else:
      male_num += 1
  school_class['students'].append({'female_num': female_num})
  school_class['students'].append({'male_num': male_num})
  female_num = 0
  male_num = 0
if school[0]['students'][2]['female_num'] > school[1]['students'][2]['female_num']:
  print(f'Больше всего девочек в классе {school[0]["class"]}')
else:
  print(f'Больше всего девочек в классе {school[1]["class"]}')

if school[0]['students'][3]['male_num'] > school[1]['students'][3]['male_num']:
  print(f'Больше всего мальчиков в классе {school[0]["class"]}')
else:
  print(f'Больше всего мальчиков в классе {school[1]["class"]}')
