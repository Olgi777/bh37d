# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
from random import randint
numbers = [randint(1,5) for _ in range(5)]
print(numbers)

result = [numbers[index - 1] + numbers[index - len(numbers) + 1] for index, element in enumerate(numbers)]
print(result)
