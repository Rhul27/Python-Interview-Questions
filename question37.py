# Program for the following requirements
# Input : 2 512
# Output : 8

# Explaination : 
# 2*2=4 4*2=8 8*2=16 .... 256*2=512
# count of the multiplication process is 8

num=input("Enter the numbers : ")
num=num.split()
a,b=num
result=2
count = 0 

while True:
    result=result*2
    count+=1
    if result==int(b):
        break
print(count)