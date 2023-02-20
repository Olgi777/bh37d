# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

from random import randint
numbers = [randint(1,10) for _ in range(10)]
print(numbers)

for i in numbers.copy():
    if i % 2 != 0:
        numbers.append(i)
        numbers.remove(i)

        print(numbers)



