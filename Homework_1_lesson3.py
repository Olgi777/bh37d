# Заполнить список степенями числа 2 (от 2^1 до 2^n)

result = []
n = 0
n = int(input("Введите количество раз возведений в степень: "))
for i in range(n):
    result = 2 ** (i+1)
    print(result)