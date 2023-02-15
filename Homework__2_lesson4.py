# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

number1 = int(input("Введи число: "))
operation = input("Введи действие:")
number2 = int(input("Введи число: "))
result = int()
# while not number1.isdigit() or not number2.isdigit():
#     number = input("Попробуйте еще раз: ")
if operation == '+':
    result = number1 + number2
    print(result)
elif operation == "-":
    result = number1 - number2
    print(result)
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
elif operation == "**":
    result = number1 ** number2
elif number2 == 0:
    print("На ноль делить нельзя!")
else:
    print("Ошибка")
print(result)
