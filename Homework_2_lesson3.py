# Написать программу, которая будет создавать словарь для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

letter_count = {}
text = input("Введите текст: ")
for i in text:
    letter_count = (i, text.count(i))
    print (letter_count)