# Date - 03/02/2023
#    *args = parameter that will pack all arguments into a tuple
#    useful so that a function can accept a varying amount of arguments -
#    - параметр, который упаковывает все аргументы в кортеж, полезный для того,
#     чтобы функция могла принимать различное количество аргументов.

def add(*args):
    sum = 0
    # args[0] = 0
    # we can't change arguments, because tuple is unchangeable
    # we should convert tuple to list
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3))