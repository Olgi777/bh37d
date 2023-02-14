
# from collections import *
#
# Counter
# number = input()
# while not number.isdigit():
#     number = input('try again: ')

# N = int(input("Введи количество чисел: "))
# M = int(input("Введи число кратности: "))
# K = int(input("Введи число больше которого твое: "))
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

N = int(input("Введи число: "))
# for number in range(2,N):
#     if number % 2 == 0:
#         print(number)

number = [number for number in range(2,N) if number % 2 == 0]
print(number)




