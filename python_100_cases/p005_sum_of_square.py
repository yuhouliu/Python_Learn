# -*-coding: utf-8-*-

'''功能：求前n个数字的平方和'''

def sum_of_square(n):
    sum = 0
    for number in range(1, n+1):
        sum = sum + number * number
    return sum

print("sum of square 3: ", sum_of_square(3))
print("sum of square 5: ", sum_of_square(5))
print("sum of square 10: ", sum_of_square(10))