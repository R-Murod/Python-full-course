# lambda function = function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression.
# (think of it as a shortcut) - думайте об этом как о ярлыке
# (useful if needed for a short period of time, throw-away) - полезно, если нужно на короткое время, одноразовый

# lambda parameters: expression

# expression -выражение

# def double(x):
#     return x * 2
#
#
# print(double(5))

double = lambda x: x * 2
print(double(2))
multiply = lambda x, y: x * y
print(multiply(2, 5))
add = lambda x, y, z: x + y + z
print(add(5, 5, 2))
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Murod", "Code"))
age_check = lambda age: True if age >= 18 else False
print(age_check(50))