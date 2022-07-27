# -*-coding: utf-8-*-

'''功能：批量合并多个txt文件'''

import os

data_dir = './datas/many_texts'   # txt文件的目录

contents = []

for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith('.txt'):
        with open(file_path, encoding='utf-8') as fin:
            contents.append(fin.read())

final_content = '\n'.join(contents)  # 将列表内容用换行符连接起来

with open('./datas/mant_text_out.txt', 'w', encoding='utf-8') as fout:
    fout.write(final_content)
