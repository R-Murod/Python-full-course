# Date - 06/02/2023
# read a file - чтение файла
try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
