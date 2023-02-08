# Написать программу, которая будет создавать словарь для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

letter_count = {}
text = input("Введите текст: ")
letter_count = {i: text.count(i) for i in text}
print(letter_count)
