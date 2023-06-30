# Ways to reverse a strings
# 1. While loop
# 2. for loop
# 3. Slicing

name=input("Enter a string : ")
# Method 1 : While Loop
r_name=""
count=len(name)
while count>0:
    r_name=r_name+name[count-1]
    count=count-1
print(f'reverse : {r_name}')


# Method 2 : for loop
r_name=""
for i in name:
    r_name=i+r_name

print(f'reverse : {r_name}')


# Method 3 : Slicing
r_name=name[::-1]
print(f'reverse : {r_name}')

