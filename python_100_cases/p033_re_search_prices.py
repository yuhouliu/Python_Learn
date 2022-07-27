# -*-coding: utf-8-*-

'''
功能：从文本中提取商品相关信息
# 要求提取 (1、黄瓜、8)、(2、葡萄、13.5)、(3、白菜、5.4)
'''

import re


content = """
小明上街买菜
买了1斤黄瓜花了8元；
买了2斤葡萄花了13.5元；
买了3斤白菜花了5.4元；
"""

pattern = re.compile(r"买了(\d)斤(.*)花了(\d+(\.\d+)?)元")

for line in content.split('\n'):
    # print(line)
    # pattern = r"买了(\d)斤(.*)花了(\d+(\.\d+)?)元"
    match_obj = pattern.search(line)
    if match_obj:
        print(f"{match_obj.group(1)}\t{match_obj.group(2)}\t{match_obj.group(3)}")
        # print(match_obj.groups())
