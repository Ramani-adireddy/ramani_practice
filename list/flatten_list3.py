
def flatten(lst):
    lst1=[]
    for i in lst:
        if isinstance(i,list):
            lst1.extend(flatten(i))
        else:
            lst1.append(i)
    return lst1
lst=[1,2,[3,4],5,6]
print(flatten(lst))
