# list comprehension = a way create a new list with less syntax can mimic certain lambda functions, easier to read
# способ создания нового списка с меньшим количеством синтаксиса может имитировать определенные лямбда-функции, которые легче читать
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]

# list comprehension - понимание списка
# expression - выражение
# define - определять

# squares = []  # create an empty list - создать пустой список
# for i in range(1, 11):  # create a for loop - создать цикл for
#     squares.append(i * i)  # define what each loop iteration should do - определить, что должна делать каждая итерация цикла
# print(squares)

# squares = [i * i for i in range(1, 11)]
# print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
# passed_students = list(filter(lambda x: x >= 60, students))
# passed_students = [i for i in students if i >= 60]  # list comprehension
passed_students = [i if i >= 60 else "Failed" for i in students if i >= 60]
print(passed_students)


