lst=[1,2,2,4,5]
lst1=[]
for i in range(len(lst)-1,-1,-1):
    lst1.append(lst[i])
print(lst1)