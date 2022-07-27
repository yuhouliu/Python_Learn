# -*-coding: utf-8-*-

'''
功能：统计中文文章分词词频
'''

content = """
春姑娘悄悄地来到了我们的校园！
绿油油的小草睁着抢着从地下探出了头，东张西望地看着四周。
池塘边的柳树，抽出了新的柳枝和柳叶，微风轻轻一吹，柳树就晃动着自己的秀发。
花园里的各种各样的花儿都开了，
有艳红的玫瑰花、粉色的桃花、雪白的梨花......五颜六色，美不胜收。
"""
import re
import jieba   #处理中文的库


content = re.sub(r"[\s。...，、！]", "", content)  # 将标点符号等替换为空

word_list = jieba.cut(content)

print(list(word_list))
