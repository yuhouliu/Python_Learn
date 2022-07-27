# -*-coding: utf-8-*-

'''功能：从列表中移除多个元素'''

def remove_elements_form_list(lista, listb):
    for item in listb:
        lista.remove(item)
    return (lista)



lista = [3, 5, 7, 9, 11, 13]
listb = [7, 11]
print(f"from {lista} remove {listb}, result: ", remove_elements_form_list(lista, listb))

####

lista = [3, 5, 7, 9, 11, 13]
listb = [7, 11]
data = [item for item in lista if item not in listb]
print(f"from {lista} remove {listb}, result: ", data)  # 列表推导式