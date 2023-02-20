#Написать функцию перевода десятичного числа в двоичное и обратно, без
#использования функции int


# def reverse(a):
#
#     #while not a.isdigit():
#     while not a:
#         print("Попробуйте еще раз: ")
#     else:
#         result = 0
#         result.append = a // 2
#         return
#         print(result)
#
#
# reverse(256)
#
#
# def dec_bin(a):
#     result = ""
#     while a:
#         y = str(a % 2)
#         result = y + result
#         a = int(a / 2)
#     print(result)
# dec_bin(100)

def bin_dec(data):
    number = 0
    data = ""
    len_dat = len(data)
    for i in range(0, len_dat):

        number += (int(data[i]) * (2**(len_dat - i -1)))
        return number
    print(number)

bin_dec(101111)