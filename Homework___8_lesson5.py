# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

words = {
            "Belarus" : ["GOMEL", " MINSK "],
            "Russia" : ["MOSKOW", "PITER"],

         }
city = input("Введи город: ")
city = city.upper()

for city in words.items():
    print(words.keys())
