# Write a python program for finding all possible substrings
# of string

# bye 
# substrings :- b,y,e,by,ye,bye

# hello
# substrings :- h,e,l,l,o,he,el,ll,lo,hel,ell,llo,hell,ello,hello

# who
# substrings :- w,h,o,wh,ho,who

str1=input("Enter a String : ")
str2= []
for i in range(0,len(str1)):
    for j in range(i+1,len(str1)+1):
        str2.append(str1[i:j])
print(str2)

