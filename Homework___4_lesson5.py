# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

objs = [4, 8, None, True, "apple", "fool", "magikan", 5]
result = [*filter(lambda obj: isinstance(obj, str), objs)]
print(result)