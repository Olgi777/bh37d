# Вывести четные числа от 2 до N по 5 в строку
N = int(input("Введи число: "))
# for number in range(2,N):
#     if number % 2 == 0:
#         print(number, end =" ")



# number = [number for number in range(2,N) if number % 2 == 0]
# print(number)

c = 0
for i in range(2, N+1, 2):
    print(i,end =" ")
    c += 1
    if c % 5 == 0:
        print()