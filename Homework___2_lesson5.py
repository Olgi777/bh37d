# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)

def morze(text: str) -> str:
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
    res = " "
    text = text.upper()
    for key in text:
        if key in dictionary:
            res += dictionary.get(key) + " "
    return dictionary


print(morze('3cCaB'))