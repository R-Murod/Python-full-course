# epoch - a date and time from which a computer measures system time - дата и время, по которым компьютер отсчитывает системное время
# representation - представление
# accepts - принимает

import time

#print(time.ctime(100000000)) # ctime() - convert a time expressed in seconds since epoch to a readable string, add a seconds

# print(time.time())  # return current seconds since epoch

# print(time.ctime(time.time()))  # current time

# time_object = time.localtime()
# print(time_object)
# local_time= time.strftime("%B %d %Y %H:%M:%S", time_object) # %B - month, %d - day etc. strftime() - string format time
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2000, 10, 20, 15, 23, 50, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string) # Mon Oct 20 15:23:50 2000

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2000, 10, 20, 15, 23, 50, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string) # 972033830.0