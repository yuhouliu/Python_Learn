# -*-coding: utf-8-*-
'''
功能：怎样递归搜索目录,返回最大内存的文件

for root, dirs, files in os.walk()
root   # 代表当前目录
dirs   # 代表当前目录下的子目录
files  # 代表当前目录下的文件
'''

import os

# 要搜索的目录
search_dir = r'D:/workspace/python_100_cases'

result_files = []
for root, dirs, files in os.walk(search_dir):
    for file in files:
        file_path = f"{root}/{file}"   # 单个文件全路径
        result_files.append((file_path, os.path.getsize(file_path)))

print(
    sorted(result_files, key=lambda x:x[1], reverse=True)[:10]
)    # 返回前10个最大的文件全路径 及 大小