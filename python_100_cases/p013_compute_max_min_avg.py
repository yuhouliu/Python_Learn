# -*-coding: utf-8-*-

'''功能：统计学生成绩文件，最高分、最低分、平均分'''


def compute_score():
    scores = []
    with open('student_grade_input.txt', encoding='utf-8') as fin:
        for line in fin:
            line = line[:-1]   # 去除换行符
            scores.append(int(line.split(',')[2]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores) / len(scores), 2)
    return max_score, min_score, avg_score


max_score, min_score, avg_score = compute_score()
print(f"max_score:{max_score}, min_score:{min_score}, avg_score:{avg_score}")