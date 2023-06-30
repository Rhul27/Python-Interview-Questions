# To check is a perfect number or not

num = int(input("Enter a Number : "))
sum1=0
for i in range(1,num):
    if num%i==0:
        sum1=sum1+i
if sum1==num:
    print('Perfect Number')
else:
    print('Not Perfect Number')