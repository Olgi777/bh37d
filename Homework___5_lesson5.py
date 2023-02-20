# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза


lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lists = list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in lists:
    my_range = []
    my_range += range(len(lists)-1, -1, -1)
print(my_range)




