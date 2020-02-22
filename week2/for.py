print('______Task_1______')
num_list = [-7, 3, 9, 81,-27, 11, -17, 3, 0,10]
for number in num_list:
    number += 1
    print(number)

print('______Task_2______')
string = input("Input a string: ")
for letter in string:
    print(letter) 

print('______Task_3______')
school_scores = [
{'school_class': '4a', 'scores':[3,4,4,5,2]},
{'school_class': '4b', 'scores':[4,4,5,3,5]},
{'school_class': '5a', 'scores':[3,2,3,5,5]},
{'school_class': '5b', 'scores':[3,3,3,4,4]},
{'school_class': '6a', 'scores':[3,2,3,4,4]}
]

scores_sum = 0
school_scores_sum = 0
middle_class_score = 0
middle_school_score = 0

for each_class in school_scores:
    for score in each_class['scores']:
        scores_sum += score
    middle_class_score = scores_sum / len(each_class['scores'])
    print(f'{each_class["school_class"]} : {middle_class_score}')
    school_scores_sum += middle_class_score
    scores_sum = 0
print(school_scores_sum)
middle_school_score = school_scores_sum / len(school_scores)
print(f'Schhol middle score: {middle_school_score}')