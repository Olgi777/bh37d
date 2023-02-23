# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

# objs = [4, 8, None, True, "apple", "fool", "magikan", 5]
# result = [*filter(lambda obj: isinstance(obj, str), objs)]
# print(result)


# Вариант 2
objs = [4, 8, None, True, "apple", "fool", "magikan", 5 ]
for i in range(len(objs) -1, -1, -1):
    if not isinstance(objs[i], str):
        del objs[i]

print(objs)