def str_comparison(first_string, second_string = 'two'):
    if type(first_string) != str and type(second_string) != str:
        return 0
    elif first_string == second_string:
        return 1
    elif len(first_string) > len(second_string):
        return 2
    elif first_string != second_string and second_string == 'learn':
        return 3

def activity(age):
    age = abs(int(age))
    if 2 <= age <= 6:
        print('Have fun in kindergarten!')
    elif 7 <= age <= 17:
        print('Study at school')
    elif 18 <= age <= 21:
        print ('Go to University')
    elif age >= 22:
        print ('Work!') 
    else:
         print ('You're too old or too young')

print('_______________FIRST_TASK_____________________')
print(str_comparison(1,2))
print(str_comparison('string','string'))
print(str_comparison('long_string','short'))
print(str_comparison('py','learn'))
print(str_comparison('one','two'))
print('____________SECOND_TASK_______________________')    
age = input('Please input your age: ')
activity(age)