# -*-coding: utf-8-*-

'''功能：计算列表数字的和'''

def sum_of_list(param_list):
    total = 0
    for item in param_list:
        total += item
    return total


list1 = [1, 2, 3, 4]
list2 = [17, 5, 3, 5]

print(f"sum of {list1}", sum_of_list(list1))
print(f"sum of {list1}", sum_of_list(list1))

print(f"sum of {list1}", sum(list1))   # python有自带 sum(list)函数计算列表元素的和
print(f"sum of {list1}", sum(list1))