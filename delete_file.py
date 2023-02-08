# Date - 08/02/2023
# delete files - удалить файлы
# permission - разрешение
# containing - содержащий

import os
import shutil

path = "copy.txt"

try:
    os.remove(path) # delete file
    os.rmdir(path) # delete directory
    shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path + " was deleted")
