# -*-coding: utf-8-*-

'''
功能：怎样实现学生成绩排序
学生成绩数据格式：复杂列表，元素是字典或元组
'''

students = [
    {"sno":101, "sname":"小张", "sgrade":88},
    {"sno":102, "sname":"小王", "sgrade":99},
    {"sno":103, "sname":"小李", "sgrade":77},
    {"sno":104, "sname":"小赵", "sgrade":66}
]

student_sort = sorted(students, key=lambda x:x["sgrade"], reverse=True)   # sorted函数中传入key,key指向一个函数

print(f"排序前：{students}")
print(f"排序后：{student_sort}")