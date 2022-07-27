# -*-coding: utf-8-*-


'''
功能：从文本中提取手机号码  正则匹配

手机号码特征：共11位数字，第一位是1，第二位是3-9之间的数字，后面9位为任意数字
'''

import re

content = """白日19989881888依山尽，黄河入45645546468798978海流。欲穷12345千里目，更上15619292345一层楼"""

pattern = r'1[3-9]\d{9}'    # 正则匹配模式

results = re.findall(pattern, content)

for result in results:
    print(result)