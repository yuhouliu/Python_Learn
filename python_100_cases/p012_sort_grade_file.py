# -*-coding: utf-8-*-

'''
功能：读取成绩文件排序数据
输入文件：
    三列：学号、姓名、成绩
    列之间用逗号分隔，比如"101,小张，88"
处理：
    读取文件，按成绩倒序排列
输出：
    排序后的三列数据
'''


def read_file():
    result = []
    with open('student_grade_input.txt', encoding='utf-8') as fin:
        for line in fin:
            line = line[:-1]  # -1代表最后一个字符，本行意思为去掉最后一个字符即换行符
            result.append(line.split(","))
    return result


def sort_grades(datas):
    return sorted(datas, key=lambda x:int(x[2]))   #按成绩排序


def write_file(datas):
    with open("student_grade_output.txt", 'w') as fout:
        for data in datas:
            fout.write(','.join(data) + '\n')  # 将列表中元素用,连接成字符串写入

# 读取文件
datas = read_file()
print(datas)

#排序数据
datas = sort_grades(datas)
print(datas)

#写入文件
write_file(datas)
