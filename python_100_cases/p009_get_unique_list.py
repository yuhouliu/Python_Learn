# -*-coding: utf-8-*-

'''功能：列表去重'''

def get_unique_list(param_list):
    result = []
    for item in param_list:
        if item not in result:
            result.append(item)
    return result



lista = [10, 20, 30, 10, 20]
print(f"source list {lista}, unique list: ", get_unique_list(lista))


print(f"source list {lista}, unique list: ", list(set(lista)))   # 利用set集合去重，再转换成list