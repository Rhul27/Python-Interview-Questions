# To display the words that are repeated more than or equal to N times in the text

str1=input("Enter the Text : ")
n=int(input("Enter the Number : "))
count=dict()
str1=str1.split()
for i in str1:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
word_lst=[]
for key in count:
    if count[key]>=n:
        word_lst.append(key)
if len(word_lst)>0:
    print(word_lst)
else:
    print("NA")

