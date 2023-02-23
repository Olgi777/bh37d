#Написать функцию перевода десятичного числа в двоичное и обратно, без
#использования функции int


# def dec_bin(a: int) -> str:
#     result = " "
#     while a > 1:
#         result = f'{a % 2}' + result
#         a //= 2
#     result = f'{a}' + result
#     return result
#
# print(dec_bin(14))

# def bin_dec(binary: str) -> int:
#     number = 0
#     for i in binary:
#         i = int(i)
#         number *= 2
#         number += i
#     return number
#
#
# print(bin_dec('1110'))