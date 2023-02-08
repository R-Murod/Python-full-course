# Date - 04/02/2023
# str.format() - optional method that gives users
# more control when displaying output - необязательный метод, который дает пользователям
# больше контроля при отображении вывода
# curly braces - фигурные скобки
# lowercase - нижний регистр
# uppercase - верхний регистр
# scientific notation - экспоненциальная запись - в информатике и вычислительной математике — представление действительных чисел в виде мантиссы и порядка.


# animal = "cow"
# item = "moon"

# print("The " + animal + " jumped ovef " + item)
# print("The {} jumped over {}".format(animal, item))
# print("The {1} jumped over {0}".format(animal, item)) # positional argument
# print("The {animal} jumped over {item}".format(animal="cow", item="moon")) # keyword argument

# name = "Murod"

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) # space to right
# print("Hello, my name is {:>10}. Nice to meet you".format(name)) # space to left
# print("Hello, my name is {:^10}. Nice to meet you".format(name)) # center

# number = 3.14159
numer_2 = 1000

# print("The number pi is {}".format(number))
# print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(numer_2))
print("The number is {:b}".format(numer_2)) # format to binary, binary - двоичная система счисления
print("The number is {:o}".format(numer_2)) # format to octal, octal - восьмиречная система счисления
print("The number is {:x}".format(numer_2)) # format to hexadecimal for lowercase, octal - щеснадцатеричная система счисления
print("The number is {:X}".format(numer_2)) # format to hexadecimal for uppercase, octal - щеснадцатеричная система счисления
print("The number is {:e}".format(numer_2)) # format to scientific notation for lowercase, octal - щеснадцатеричная система счисления
print("The number is {:E}".format(numer_2)) # format to scientific notation for uppercase, octal - щеснадцатеричная система счисления