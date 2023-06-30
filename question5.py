#Count a vowel in a string

name=input('Enter a name : ')      
count=0
for i in name.lower():
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(count)
