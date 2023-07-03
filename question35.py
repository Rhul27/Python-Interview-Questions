# Print character by the times of occurence
# Input : 'abcaba'
# Output : abcaabbaaa


str1 = 'abcaba'
dict1 = {}
for i in str1:
    if i not in dict1:
        dict1[i]=1  
        print(i,end='') 
    else:
        dict1[i]=dict1[i]+1
        print(i*dict1[i],end='')

