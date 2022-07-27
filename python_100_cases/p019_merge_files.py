# -*-coding: utf-8-*-
'''功能：实现不同文件之间的数据关联'''

course_teacher_map = {}
with open('./datas/course_teacher.txt', encoding='utf-8') as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(',')
        course_teacher_map[course] = teacher

print(course_teacher_map)   # 返回课程<->老师之间的映射关系

with open('course_student_grade_input.txt',encoding='utf-8') as fin:
    for line in fin:
        line = line[:-1]
        course, sno, sname, grade = line.split(',')
        teacher = course_teacher_map[course]
        print(course, teacher, sno, sname, grade)  # 最后将该值写入文件即可