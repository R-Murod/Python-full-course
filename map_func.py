# map() = applies a function to each item in an iterable (list, tuple, etc.)
# применяет функцию к каждому элементу в итерируемом объекте (список, кортеж и т. д.)
# map(function, iterable)

# apply - применяет
# shirt - рубакшка
# pants - брюки
# jacket - куртка
# socks - носки
# untouched - нетронутый

store = [("shirt", 20.20),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("Socks", 10.00)]
to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], data[1] / 0.82)
store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)