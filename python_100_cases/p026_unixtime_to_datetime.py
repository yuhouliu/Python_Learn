# -*-coding: utf-8-*-
'''
功能: 将unix时间戳转换成格式化时间
'''

import datetime

unix_time = 1620747647

unix_time_obj = datetime.datetime.fromtimestamp(unix_time)  #将时间戳转换为时间对象
datetime_str = unix_time_obj.strftime("%Y-%m-%d %H:%M:%S")  # 格式化时间字符串
print(datetime_str)