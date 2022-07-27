# -*-coding: utf-8-*-

'''功能：计算不同课程的最高分、低分和平均分'''

# key: course, value: grade list
course_grades = {}

with open('course_student_grade_input.txt', encoding='utf-8') as fin:
    for line in fin:
        line = line[:-1]
        course, sno, sname, grade = line.split(',')
        if course not in course_grades:
            course_grades[course] = []  # 赋初值
        course_grades[course].append(int(grade))

print(course_grades)

for course, grade in course_grades.items():
    print(course, max(grade), min(grade), sum(grade)/len(grade))


