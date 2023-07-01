# Alternate the case of each letter in a given string
# First letter must be uppercase !!

# Method 1 :
# str1=input("Enter the string : ")
# str2=""
# i=0
# while i<len(str1):
#     if i==0:
#         str2=str2+str1[i].upper()
#     else:
#         str2=str2+str1[i].swapcase()
#     i+=1
# print(str2)

# Method 2 : Without python functions

str1=input("Enter the string : ")
def func(str1):
    str2=""
    asc=ord(str1[0])
    if asc>=97 and asc<=122:
        str2=str2+chr(asc-32)
    else:
        str2=str2+str1[0]

    for ch in str1[1:]:
        if ord(ch)>=97 and ord(ch)<=122:
            str2=str2+chr(ord(ch)-32)
        else:
            str2=str2+chr(ord(ch)+32)
    print(str2) 
func(str1)