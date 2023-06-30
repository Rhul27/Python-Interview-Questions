# To sort character and number so that first alphabets and then numbers are printed

str1=input("Enter the String : ")
alpha=[]
num=[]
for i in str1:
    if i.isalpha():
        alpha.append(i)
    else:
        num.append(i)

final=sorted(alpha)+sorted(num)
print("".join(final))