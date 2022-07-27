# -*-coding: utf-8-*-
'''
功能：统计目录下的所有文件大小
'''


import os

print(os.path.getsize('article.txt'))   # os.path.getsize(file)  返回文件的大小

sum_size = 0
for file in os.listdir():
    if os.path.isfile(file):   # 只判断文件，舍弃目录
        # print(file)
        sum_size += os.path.getsize(file)

print(f'all size of dir is: {sum_size} byte')
print(f'all size of dir is: {sum_size/1000} KB')