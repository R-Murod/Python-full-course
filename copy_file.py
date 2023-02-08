# Date - 08/02/2023
# copy a file - скопировать файл
# copyfile() = copies contents of a file - копирует содержимое файла
# copy() = copyfile() + permission mode (режим разрешения) + destination can be a directory (назначение может быть каталогом)
# copy2() = copy() + copies metadata (file's creation and modification times) - копирует метаданные (время создания и модификации файла)
# source - источник
# destination - место назначения

import shutil

# shutil.copyfile('test.txt', 'C:\\Users\\Камбаралиев Ахрорали\\Desktop\\copy.txt') # src, dst
# shutil.copy('test.txt', 'C:\\Users\\Камбаралиев Ахрорали\\Desktop\\copy.txt')  # src, dst
shutil.copy2('test.txt', 'C:\\Users\\Камбаралиев Ахрорали\\Desktop\\copy.txt') #  src, dst
