# Date - 06/02/2023
# file detection - обнаружение файла
# exists - существует
# Модуль os в Python — это библиотека функций для работы с операционной системой.

import os

path = "C:\\Users\\Камбаралиев Ахрорали\\Desktop\\test.txt"
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")
