# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
sum_a = 0
word = 'Архангельск'
for letter in word.lower():
    if letter == 'а':
        sum_a += 1
print(sum_a)

# Вывести количество гласных букв в слове
vowel = 0
word = 'Архангельск'
for letter in word.lower():
    if letter in ['а','е','ё','и','о','у','э','ю','я']:
        vowel += 1
print(vowel)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
word_sum = len(sentence.split())
letter_sum = 0
for word in sentence.split():
    letter_sum += len(word)
print( letter_sum / word_sum)
