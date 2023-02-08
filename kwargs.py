# Date - 03/02/2023
#    *kwargs = parameter that will pack all arguments into a dictionary
#    useful so that a function can accept a varying amount of arguments -
#    - параметр, который упаковывает все аргументы в словарь, полезный для того,
#     чтобы функция могла принимать различное количество аргументов.
# useful - полезный

# def hello(**kwargs):
#     for key, value in kwargs.items():
#         print(value)
#
#
# hello(first="Bro",middle="Hey", last="Code")

# def arg_printer(a, b, option=True, **kwargs):
#    print(a, b)
#    print(option)
#    print(kwargs)
#
#
# arg_printer(3, 4, param1=5, param2=6)

# 3 4
# True
# {'param1': 5, 'param2': 6}