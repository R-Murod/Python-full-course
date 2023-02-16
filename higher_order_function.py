# higher order function - функция высшего порядка
# Higher Order Function = a function that either:
# 1. accepts a function as an argument - принимает функцию в качестве аргумента
# or
# 2. returns a function (In python, functions are also treated as objects) - возвращает функцию (в python функции также рассматриваются как объекты)

# either - либо, или
# loud - громкий
# quiet - тихий
# divisor - делитель
#

# example for first
# def loud(text):
#     return text.upper()
#
#
# def quiet(text):
#     return text.lower()
#
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
#
# hello(loud)
# hello(quiet)

def divisor(x):  # divisir high order function, because we're returning dividend
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))