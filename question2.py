# To reverse internal string
str1="python is easy"
# output="nohtyp si ysae"
str2=str1.split(" ")
str3=[]
for i in str2:
    str3.append(i[::-1])

final=" ".join(str3)
print(final)

