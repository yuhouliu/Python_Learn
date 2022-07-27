# -*-coding: utf-8-*-

'''功能：怎样计算两个日期相隔的天数'''

import datetime

birthday = "1991-12-20"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")   #字符串转时间对象 datetime.datetime.strptime()
print(birthday_date, type(birthday_date))

curr_datetime = datetime.datetime.now()
print(curr_datetime, type(curr_datetime))

minus_datetime = curr_datetime - birthday_date # 当前日期时间对象- 生日日期时间对象
print(minus_datetime, type(minus_datetime))

print(minus_datetime.days)   # 返回具体的天数