""" a = 2
b = 0.5
print(a+b)

first_name = 'anna'
last_name = 'Kozeev@'
print(f'Привет,{first_name.capitalize()} {last_name.replace("@","a")}')

template = 'Привет, {user}'.format(user=first_name.capitalize())
print(template)

v = int(input('Введите число от 1 до 10: '))
print(v+10)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?') """

""" num_list = [3,5,7,9,10.5]
print(num_list)
num_list.append('Python')
print(num_list)
print(len(num_list))

print(num_list[0])
print(num_list[-1])
print(num_list[1:4])
num_list.remove('Python')
print(num_list) """

dict = {"city": "Москва", "temperature": "20"}
print(dict["city"])
updated_temperature = int(dict["temperature"]) - 5
dict["temperature"] = str(updated_temperature)
print(dict)
print("")
print(dict.get("country"))
print(dict.get("country", "Россия"))
dict["date"] = "27.05.2019"
print(dict)
print(len(dict))