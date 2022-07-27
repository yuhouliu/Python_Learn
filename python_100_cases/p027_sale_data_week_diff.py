# -*-coding: utf-8-*-

'''
功能：计算日期数据周同比，即将日期的销售额和7天前的销售额相减除以7天前的销售额
'''

import datetime

def get_diff_days(date, days):
    curr_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    timedelta = datetime.timedelta(days=-days)
    return (curr_date + timedelta).strftime("%Y-%m-%d")



data_sale = {}   # 日期、销售额字典
is_first_line = True
with open("./datas/date_sale_data.txt", encoding='utf-8') as fin:
    for line in fin:
        if is_first_line:    # 第一行文字 去除
            is_first_line = False
            continue
        line = line[:-1]  # 去除最后一行
        date, sale_number = line.split('\t')
        # print(date, sale_number)
        data_sale[date] = float(sale_number)

for date, sale_number in data_sale.items():
    date7 = get_diff_days(date, 7)  # 获取7天前日期
    sale_number7 = data_sale.get(date7, 0)   # 获取7天前的销售额，若不存在则为0
    if sale_number7 == 0:
        print(date, sale_number, 0)
    else:
        week_diff = round( (sale_number-sale_number7)/sale_number7, 4 ) # round(number, 4) 保留4为小鼠
        print(date, sale_number, date7, sale_number7, week_diff)