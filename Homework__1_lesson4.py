# Вывести первые N чисел кратные M и больше K

# N = int(input("Введи количество чисел: "))
# M = int(input("Введи число кратности: "))
# K = int(input("Введи число больше которого твое: "))
# numbers = []
# for n in range(100000000000):
#     if n % M == 0 and n > K:
#         numbers.append(n)
#         if len(numbers) == N:
#             break
# print(numbers)
N = int(input("Введи количество чисел: "))
M = int(input("Введи число кратности: "))
K = int(input("Введи число больше которого твое: "))
while N:
    if K % M ==0:
        N-= 1
        print(K, end=" ")
        K +=M
    K+= 1