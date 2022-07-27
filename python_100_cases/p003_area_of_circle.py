# -*-coding: utf-8-*-

'''功能：计算圆的面积'''

import math

def computer_area_of_circle(r):
    return( round(math.pi * r * r, 2) )   # round保留2为小数


print("area of 2 is: ", computer_area_of_circle(2))
print("area of 3.14 is: ", computer_area_of_circle(3.14))
print("area of 6.78 is: ", computer_area_of_circle(6.78))
