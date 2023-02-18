# sort() method = used with lists
# sort() function = used with itarebles

students = [("Murod", "F", 60),
            ("Farkhod", "A", 33),
            ("Bahadir", "D", 36),
            ("Javohir", "B", 20),
            ("Mr.Bobs", "C", 78)]  # we will use key for sort list a tuple

# students = (("Murod", "F", 60),
#             ("Farkhod", "A", 33),
#             ("Bahadir", "D", 36),
#             ("Javohir", "B", 20),
#             ("Mr.Bobs", "C", 78))  # we use method sorted() in tuple

# grade = lambda grades: grades[1] # that's function we use for interrupted
# students.sort(key=grade)

age = lambda ages: ages[2]
# students.sort(key=age, reverse=True)
sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)
