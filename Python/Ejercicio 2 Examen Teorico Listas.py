lis=[11,7,12,10,13,9,8]

a=min(lis)
b=max(lis)

lis[lis.index(a)]=lis[0]
lis[0]=a
lis[lis.index(b)]=lis[len(lis)-1]
lis[len(lis)-1]=b

print(lis)
