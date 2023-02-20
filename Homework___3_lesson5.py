# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

from random import randint
def removal(numbers, N):
    if N < 0:
        N = abs(N)
        for i in range(N):
            numbers.append(numbers.pop(0))
            print(numbers)
    else:
        for i in range(N):
            numbers.insert(0, numbers.pop())
            print(numbers)
    pass

numbers = [randint(1,10) for _ in range(10)]
print(numbers)
N = int(input("Введи шаг: "))
removal(numbers, N)


