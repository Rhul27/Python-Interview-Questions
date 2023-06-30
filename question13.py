# Fibonacci Series

# Method 1 : for loop
n=int(input('Enter a number : '))
first=0
second=1
if n<=0:
    print("Enter a larger number")
elif n==1:
    print(first)
else:
    for i in range(n+1):
        print(first,end=" ")
        temp=first
        first=second
        second=temp+first

# Method 2 : While Loop

n=int(input('Enter a number : '))
first=0
second=1
count=0
if n<=0:
    print("Enter a larger number")
elif n==1:
    print(first)
else:
    while count<=n:
        print(first,end=" ")
        temp=first
        first=second
        second=temp+first
        count+=1


