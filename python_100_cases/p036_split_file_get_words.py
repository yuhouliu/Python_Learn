# -*-coding: utf-8-*-

# coding:utf-8
'''
功能：统计英文文章单词词频

'''


import re
import pandas as pd

with open('english_article.txt') as fin:
    content = fin.read()

# print(content.split())

words = re.split(r"[\s.()-?]", content)   # 用正则匹配模式去分割字符串，只要出现空格、点、括号、减号、问号都会分割

print(pd.Series(words).value_counts()[:5])   # pd.Serise(words).value_counts 使用pandas对list中元素做词频统计， 取前5个值