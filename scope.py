# Date - 03/02/2023
# scope = The region that a variable is recognized. Область, в которой распознается переменная
# A variable is only available from inside the region it is created. Переменная доступна только внутри региона, в котором она создана.
# A global and locally scoped versions of a variable can be created. Можно создать глобальную и локальную версии переменной.
# scope - область видимость
# LEGB - Top 4 Types of Scope
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

name = "Bro"  # global scope


def display_name():
    name = "Code"  # local scope
    print(name)


display_name()
print(name)
