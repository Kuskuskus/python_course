def ask_user():
    answer = ''
    while answer != 'Хорошо':
        answer = input('Как дела?')

    conversation = {
        'Как дела?': 'Хорошо',
        'Что делаешь?': 'Программирую',
        'На чем программируешь?': 'На питоне'}
    question = input('Задай мне вопрос')
    while question in conversation:
        print(conversation[question])
        question = input()

ask_user()