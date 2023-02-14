# Вывести четные числа от 2 до N по 5 в строку
N = int(input("Введи число: "))
for number in range(2,N):
    if number % 2 == 0:
        print(number, end =" ")



# number = [number for number in range(2,N) if number % 2 == 0]
# print(number)