# Date - 06/02/2023
# write a file - тема о создание и добавление текста

text = "Good job"
# 'w' - изменить текст файла
# 'a' - добавляет текст к существующим текста
with open('test.txt', 'a') as file:
    file.write(text)
