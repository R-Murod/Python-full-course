# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
# применить функцию к итерации и уменьшить ее до одного кумулятивного значения
# performs function on first two elements and repeats process until 1 value remains
# выполняет функцию для первых двух элементов и повторяет процесс, пока не останется 1 значение

# reduce(function, iterable)

import functools

# letters = ["H", "e", "l", "l", "o"]
# word = functools.reduce(lambda x, y: x + y, letters)  # сложить первые два элемента, letters = ["He", "l", "l", "o"], и так продолжается
# print(word)


factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)
