#Print duplicate in the list
lst=[2,4,8,3,4,6,9,3,2,5,3]


#Method 1 : With using Built in method
lst2=[]
for i in lst:
    if lst.count(i)>1 and i not in lst2:
        lst2.append(i)
print(lst2)

#Method 2 : Without using Built in method
lst2=[]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j] and lst[i] not in lst2:
            lst2.append(lst[i])
print(lst2)
    

