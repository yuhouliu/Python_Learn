# -*-coding: utf-8-*-

'''
功能：按文件后缀整理文件夹
小知识：怎样获取文件后缀名？
    import os
    os.path.splitext('/path/to/aaa.mp3')
    输出：('/path/to/aaa', '.mp3')
小知识：怎么移动文件？
    import shutil
    shutil.move("aaa.txt", "dir/bbb")

'''

import os
import shutil
dir = "./arrange_dir"   # 目录路径

for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]  # 获取文件名后缀，eg:.txt
    ext = ext[1:]   # 去除后缀的.号
    # if not os.path.isdir(f"{dir}/{ext}"):   # 如果后缀文件夹名不存在，则创建
    #     os.mkdir(f"{dir}/{ext}")
    print(file, ext)
    ### 将对应的文件移入相应的后缀文件夹 ###
    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(source_path, target_path)