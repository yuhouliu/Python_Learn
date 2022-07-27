# -*-coding: utf-8-*-
'''功能：计算数字范围内的所有偶数'''


def get_even_numbers(begin, end):
    result = []
    for number in range(begin, end):
        if number % 2 == 0:
            result.append(number)
    return result

begin = 4
end = 15
print(f"begin={begin}, end={end}, even numbers: ", get_even_numbers(begin, end))

data = [item for item in range(begin, end) if item % 2 == 0]   # 使用列表推导式输出
print(f"begin={begin}, end={end}, even numbers: ", data)