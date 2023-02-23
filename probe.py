
# from collections import *
#
# Counter
# number = input()
# while not number.isdigit():
#     number = input('try again: ')

# N = int(input("Введи количество чисел: "))
# M = int(input("Введи число кратности: "))
# K = int(input("Введи число больше которого твое: "))
# while N:
#     if K % M ==0:
#         N-= 1
#         print(K, end=" ")
#         K +=M
#     K+= 1
# nambers = []
# for n in range(100000000000):
#     if n % M == 0 and n > K:
#         nambers.append(n)
#         if len(nambers) == N:
#             break
# print(nambers)

# number1 = input("Введи число: ")
# operation = input("Введи действие:")
# number2 = input("Введи число: ")
# result = int()
# while not number1.isdigit() or not number2.isdigit():
#     number = input("Попробуйте еще раз: ")
#     if operation == '+':
#         result = number1 + number2
#         print(result)
#     elif operation == "-":
#         result = number1 - number2
#         print(result)
#     elif operation == "*":
#         result = number1 * number2
#     elif operation == "/":
#         result = number1 / number2
#     elif operation == "**":
#         result = number1 ** number2
#     elif number2 == 0:
#         print("На ноль делить нельзя!")
#     else:
#         print("Ошибка")
#     print(result)
from pprint import pprint

# N = int(input("Введи число: "))
# for number in range(2,N):
#     if number % 2 == 0:
#         print(number)

# number = [number for number in range(2,N) if number % 2 == 0]
# print(number)

#
# class RegisterForm
#
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#
#     def is_valid(self):
#         if len(self.login) < 4 or not self.login.isalnum():
#             return False
#         if len(self.password) < 8 or self.password.isalnum():
#             return False
#         else:
#             return False

# class Product
#     def __init__(self, name:str, descr:str, prise:float):
#         if not isinstance(name, str):
#             raise TypeError
#         if not isinstance(descr, str):
#             raise TypeError
#         if not isinstance(prise, float):
#             raise TypeError
#         if len(name) < 4:
#             raise ValueError
#         if prise <= 0:
#             raise ValueError
#
#         self.name = name
#         self.descr = descr
#         self.prise = prise
#
#     def discount(self, percent):
#         if not isinstance(percent, (int, float)):
#             raise TypeError
#         elif 0 > percent or percent > 25:
#             raise ValueError
#         return self.prise * (percent / 100)
#
#     def edit_descr(self, descr: str):
#         if not isinstance(descr, str):
#             raise TypeError
#         self.descr = descr
#
class Paginator:
     objs:list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
     paginate_by:int = 3

     @classmethod
     def get_page(cls, page:int) -> list[str]:
         return cls.objs[
             (page-1) * cls.paginate_by:(page-1) * cls.paginate_by + cls.paginate_by
         ]

print(Paginator.get_page(2))
# Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле





















