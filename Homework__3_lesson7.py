# Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError

class Category:

    categories = ["Dogs", "Cats", "Birds"]

    @classmethod
    def add(cls, name_category: str):
        self.name_category = name_category
        if self.name_category not in categories:
            categories.append(self.name_category)
            return
        else:
            return ValueError
    @classmethod
    def get(cls, i: int):
        for i in range(len(categories)):
            return categories[i]
        else:
            return IndexError

    @classmethod
    def delete(cls, j: int):
        for j in categories:
            del categiries[j]

    @classmethod
    def update(cls, t: int, new_name: str):
        if t not in categories[t]:
            if new_name not in categories:
                categiries.append(new_name)
            else:
                return ValueError











