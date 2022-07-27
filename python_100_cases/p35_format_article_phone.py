# -*-coding: utf-8-*-

'''
功能：进行多种日期格式的标准化
'''

# 目标：2021-05-28
content = """
    白日2021/05/26依山尽，黄河2021.05.27入海流。
    欲穷05-28-2020千里目，更上5/29/2020一层楼。
"""

import re

# 格式化第一个时间格式
content = re.sub(r"(\d{4})/(\d{2})/(\d{2})", r"\1-\2-\3", content)    # 分组匹配，前面加小括号分组，后面替换成分组
print(content)
# 格式化第二个时间格式
content = re.sub(r"(\d{4})\.(\d{2})\.(\d{2})", r"\1-\2-\3", content)
print(content)
# 格式化第三个时间格式
content = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", content)
print(content)
# 格式化第四个时间格式
content = re.sub(r"(\d{1})/(\d{2})/(\d{4})", r"\3-0\1-\2", content)
print(content)
