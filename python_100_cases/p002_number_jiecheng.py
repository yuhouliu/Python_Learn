# -*-coding: utf-8-*-

'''功能：计算数字的阶乘'''

def get_jiecheng(number):
    result = 1
    while number > 0:
        result = result * number
        number -= 1
    return result

print("jiecheng 6 = ", get_jiecheng(6))
print("jiecheng 3 = ", get_jiecheng(3))
print("jiecheng 100 = ", get_jiecheng(100))