# -*-coding: utf-8-*-

'''功能：怎样获取当前的日期时间'''


import datetime

curr_datetime = datetime.datetime.now()   # 获取当前的日期时间

print(curr_datetime, type(curr_datetime))   # curr_datetime 是一个对象

str_time = curr_datetime.strftime('%Y-%m-%d %H:%M:%S')  # 格式化日期时间,返回是字符串
print("str_time:", str_time)


# 另外一种获取方式
print("year", curr_datetime.year)
print("month", curr_datetime.month)
print("day", curr_datetime.day)
print("hour", curr_datetime.hour)
print("minute", curr_datetime.minute)
print("second", curr_datetime.second)
