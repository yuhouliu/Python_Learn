# -*-coding: utf-8-*-
'''功能：计算开始和结束范围内的所有日期'''

import datetime


def get_date_range(begin_date, end_date):
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date_object = datetime.datetime.strptime(begin_date, '%Y-%m-%d')
        days1_timedelta = datetime.timedelta(days=1)   # 1天时间对象
        begin_date = (begin_date_object + days1_timedelta).strftime('%Y-%m-%d')
    return date_list



begin_date = '2022-03-29'
end_date = '2022-04-03'
print(get_date_range(begin_date, end_date))
