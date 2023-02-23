# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

words = {
            "Belarus" : ["GOMEL", " MINSK "],
            "Russia" : ["MOSKOW", "PITER"],

         }
city = input("Введи город: ")
city = city.upper()

for country, cities in words.items():
    if city in cities:
        print(country)
        break


    print(country)


#Вар2
# country = [*filter(lambda x: city in x [1], words.items()), [0], [0]]
# print(country)




