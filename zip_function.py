# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
# агрегировать элементы из двух или более итераций (список, кортежи, наборы и т. д.)
# creates a zip object with paired elements in tuples for each elements
# создает zip-объект с парными элементами в кортежах для каждого элемента


# dude - чувак
# guest - гость
# such as - такой как

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")

# users = zip(usernames, passwords)
# print(type(users)) # class zip

# users = list(zip(usernames, passwords))
# print(type(users)) # class list

# users = dict(zip(usernames, passwords))
# print(type(users))  # class dict
#
# for key, value in users.items():
#     print(key + " : " + value)

# two or more iterables

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)