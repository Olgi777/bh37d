

# my_file = open("my_file.txt", "r", encoding= "utf-8")
# lines = [i.strip() for i in my_file]
# result = 0
# for i in lines:
#     if i.isdigit():
#         result = int(i) + result
# print(result)
# my_file.close()


from pydantic import BaseModel, Field
from pydantic.types import Decimal
class ProductModel(BaseModel):
    title: str
    descr: str = Field(default=None)
    price: Decimal = Field(max_digits=6, decimal_places=2)

from csv import DictReader, DictWriter

invalid_products = []
with open("products.csv", "r", encoding="utf-8") as file:
    reader = DictReader(file)
    for product in reader:
        try:
            product = ProductModel(**product)
        except Exception:
            invalid_products.append(product)
with open("invalid_products.csv", "w", encoding="utf-8") as file:
    writer = DictWriter(file, fieldnames=("title", "descr", "price"))
    writer.writeheader()
    writer.writer()

