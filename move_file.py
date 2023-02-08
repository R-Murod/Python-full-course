# Date - 08/02/2023
# move a file - переместить файл
# we can move a file from project folder to my desktop - мы можем переместить файл из папки проекта на рабочий стол

import os

source = "C:\\Users\\Камбаралиев Ахрорали\\Desktop\\move_test.txt" # also we can move folder
destination = "C:\\Users\\Камбаралиев Ахрорали\\python\\python_course\\python_full_course\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")
