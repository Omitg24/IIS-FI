def ambas_l(l1,l2):
    result=[]
    for elem in l1:
        if elem not in result and elem in l2:
            result.append(elem)
    return result

l1=[1,6,6,5,2,8]
l2=[2,8,8,6]
result=ambas_l(l1,l2)
print(result)