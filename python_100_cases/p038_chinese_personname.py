# -*-coding: utf-8-*-

'''
功能：统计中文文章或小说中的人名
'''

content = "李明喜欢韩梅梅，她俩早恋了"

import jieba.posseg as posseg

for word, flag in posseg.cut(content):        # word代表人名，flag代表名词属性
    if flag == "nr":
        print(word,flag)
