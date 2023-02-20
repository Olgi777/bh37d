# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)

def morze(text):
    text = str(text)
    dictionary = {
                    "A" : ".-",
                    "B" : "-...",
                    "C" : "-.-.",
                    "D" : "-..",
                    "1" : ".----",
                    "2" : "..---",
                    "3" : "...--"
    }
    res = ""
    text = text.upper()
    for key in text:
        if key == "A":
            print(key, dictionary[key])
        elif key =="B":
            print(key, dictionary[key])
        elif key == "C":
            print(key, dictionary[key])
        elif key =="D":
            print(key, dictionary[key])
        elif key =="1":
            print(key, dictionary[key])
        elif key =="2":
            print(key, dictionary[key])
        elif key =="3":
            print(key, dictionary[key])

    print(res)
morze('3cCaB')