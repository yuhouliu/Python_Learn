# -*-coding: utf-8-*-

'''
功能：将文章中的手机号码实现打马赛克效果

re.sub
'''

content = """
白日19989881888依山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15619292345一层楼
"""


import re

pattern = r"(1[3-9])\d{9}"

result = re.sub(pattern, r"\1*****", content)    # \1 在这里代表匹配第一个分组

print(result)
