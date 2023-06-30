# 'a3b2c4' --> aaabbcccc

str1=input("Enter a string as [a3b2c4] : ")
output=""
for i in str1:
    if i.isalpha():
        var=i
    else:
        output=output+(int(i)*var)
print(output)

# 'aaabbcccc' --> 3a2b4c

str1=input("Enter a string as [aaabbcccc] : ")
output=""
char=str1[0]
count=0
for i in str1:
    if i==char:
        count+=1
    else:
        output=output+char+str(count)
        count=1
        char=i

output=output+char+str(count)
print(output)