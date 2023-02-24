# thread - a flow of execution. Like a separate order of instructions. - поток исполнения. Вроде отдельный приказ инструкции.
# However, each thread takes a turn running to achieve concurrency - Однако каждый поток работает по очереди для достижения параллелизма.
# GIL = (global interpreter lock), allows only one thread to hold the control of the Python interpreter
# позволяет только одному потоку управлять интерпретатором Python

# cpu bound (привязка к процессору) = program/task spends most of it is time waiting for internal events (CPU intensive) use multiprocessing
# программа/задача тратит большую часть времени на ожидание внутренних событий (интенсивное использование процессора) использует многопроцессорность

# io bound = program/task spends most of it is time waiting for external events (user input, web scraping) use multiprocessing
# программа/задача тратит большую часть времени на ожидание внешних событий (ввод данных пользователем,
# просмотр веб-страниц) использовать многопроцессорность

# sequentially - последовательно
# synchronise - синхронизировать

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=()) # target - will charge with function, args() - for arguments
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# Main thread is charge in x, y and z of creating

# These threads to synchronise
x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter()) # will return how long it is our calling thread in our main thread
