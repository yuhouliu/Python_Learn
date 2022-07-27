# -*-coding: utf-8-*-
'''功能：计算任意日期  n天前的日期'''


import datetime

def get_diff_days(pdate, days):
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")  # 任意日期时间对象
    time_gap = datetime.timedelta(days=days)    # 间隔天数的时间对象
    pdate_result = pdate_obj - time_gap
    return pdate_result.strftime('%Y-%m-%d')


print(get_diff_days('2022-04-28',3))
print(get_diff_days('2022-04-28',30))
print(get_diff_days('2022-04-28',7))
print(get_diff_days('2022-04-01',3))