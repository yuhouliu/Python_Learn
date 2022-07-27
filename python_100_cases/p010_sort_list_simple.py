# -*-coding: utf-8-*-

'''功能：怎样对简单列表元素排序,list.sort()或sorted(list)'''



lista = [20, 40, 30, 50, 10]

listb = lista
listb.sort()   # 不改变lista
print(f"lista is sorted {listb}")

listb = sorted(lista)
print(f"lista is sorted {listb}")


##### 倒序 reversed=True ######
listb = lista
listb.sort(reverse=True)   # 不改变lista
print(f"lista is sorted {listb}")

listb = sorted(lista,reverse=True)
print(f"lista is sorted {listb}")