def ask_user():

    conversation = {
        'Как дела?': 'Хорошо',
        'Что делаешь?': 'Программирую',
        'На чем программируешь?': 'На питоне'}
    question = input("Задай мне вопрос: ")
    while True:
        try:
            if question in conversation:
                print(conversation[question])
                question = input()
            else:
                print('Я не понимаю, задай другой вопрос')
                question = input()
        except KeyboardInterrupt:
            print('Пока!')
            break


def discounted(price, discount, max_discount=20):
    try:
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except TypeError:
        print('Строковые данные, нужно число')

ask_user()
discounted(100, 'цена')
discounted('цена', 5)

