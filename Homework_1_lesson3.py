# Заполнить список степенями числа 2 (от 2^1 до 2^n)

result = []
n = 0
n = int(input("Введите количество раз возведений в степень: "))
result = [2 ** (i+1) for i in range(n)]
print(result)


