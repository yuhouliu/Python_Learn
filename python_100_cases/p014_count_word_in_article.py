# -*-coding: utf-8-*-

'''功能：统计英语文章中每个单词出现的次数'''


word_count = {}

with open('article.txt') as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0   # 相当于给每个单词赋初值0
            word_count[word] += 1

print(f"每个单词出现次数统计: {word_count}")

# 输出统计词频最高的10个单词
print(
    sorted(
        word_count.items(),           # dict.items() 将字典变为list
        key = lambda x:x[1],
        reverse=True
    )[:10]
)
