# Date - 04/02/2023
# exception - events detected during execution that interrupt the flow of a program
# исключениe - события, обнаруженные во время выполнения, которые прерывают ход программы
# event - событие
# detect - обнаружить
# numerator - числитель
# denominator - знаменатель
# try - пытаться
# except - кроме, исключая
# divide - разделять
# idiot - идиот
# division by zero - деление на ноль
# handle it - справиться
# opportunity - возможность
# execute - выполнять

try:
    numerate = int(input("First number: "))
    denominator = int(input("First number: "))
    result = numerate / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")