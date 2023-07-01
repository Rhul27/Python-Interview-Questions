# Extract numbers from the given string
# Input : "AC*wv12n/:#e123we2.45oin (fwoi6n#a98nfwb+owi"
# Output : [2.45,6,12,98,123]

str1 = "AC*wv12n/:#e123we2.45oin (fwoi6n#a98nfwb+owi"
temp = ""
data=[]
for ch in str1:
    if ch.isdigit() or (ch=='.' and '.' not in temp):
        temp=temp+ch
    elif len(temp)!=0:
        data.append(eval(temp))
        temp=""
    
print(data)

