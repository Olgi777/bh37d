# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

students = {"id_1": {"name": "Olya", "surname": "Ivanova", "phone": "234568", "email": "olya@info.com"},
            "id_2": {"name": "Dmitri", "surname": "Petrov", "phone": "523789", "email": " "},
            "id_3": {"name": "Katya", "surname": "Goncharova", "phone": "369258", "email": "katua@info.com"},
            "id_4": {"name": "Evgeni", "surname": "Potapov", "phone": "741852", " ": "evgeni@info.com"}
            }
for student in students.values():
    # if not student.get("email"):
    if student.get("email") == " " or "email" not in student or student.get("email") is None:

        print(student.get("name"))