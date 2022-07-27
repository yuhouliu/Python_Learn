# -*-coding: utf-8-*-
'''
功能：从文本中提取电子邮箱地址
特征：
第一部分：可以是字母数字下划线中划线
第二部分：@符号
第三部分：字母数字
第四部分：.符号
第五部分：2-4个字母
'''

import re

content = """
寻隐者12345@qq.com不遇
朝代：唐asdf12dsa#abc.com代
作python666@163com者：贾岛
松下问童子，言师python-abc@163.com采药去。
只在python_anr-666@sina.net此山中，云深不知处。
"""

# 经过编译后的正则表达式对象
pattern = re.compile(r"""
[a-zA-Z0-9_-]+
@
[a-zA-Z0-9]+
\.
[a-zA-Z]{2,4}
""", re.VERBOSE)      # re.VERBOSE 允许正则表达式换行

results = pattern.findall(content)
for result in results:
    print(result)
