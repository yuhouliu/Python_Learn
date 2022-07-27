# -*-coding: utf-8-*-
'''
功能： 批量提取网页上所有的手机号码
解析: 将网页内容复制到一个txt文件中，然后读txt文件内容，做正则模式匹配
'''

import re

# 读文件
with open('webpage_phone_numbers.txt', encoding='utf-8') as fin:
    content_str = fin.read()

# 正则匹配
pattern = r'1[3-9]\d{9}'

results = re.findall(pattern, content_str)

print(len(results))
for result in results:
    print(result)
