# Create a table for any  number
flag=True
while flag:
    num=int(input("Enter a number : "))
    for i in range(1,11):
        print(f'{num} * {i} = {num*i}')
    ans=input("Do u want to continue (y/n) : ").lower()
    if ans=='y':
        flag=True
    else:
        flag=False
