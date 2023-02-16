# walrus operators :=
# new to Python 3.8
# assignment expression aka walrus operator - выражение присваивания, также известное как оператор моржа
# assigns values to variables as part of a larger expression - присваивает значения переменным как часть большего выражения

# happy = True
# print(happy)

# print(happy := True)

# foods = []
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = []
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
