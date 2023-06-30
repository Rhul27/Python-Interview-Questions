# Swapping Content between 2 variables 
a=10
b=20
# Method 1 : 

a,b=b,a
print(a,b)

# Method 2 : With Temp variable

temp=a
a=b
b=temp
print(a,b)


# Method 3 : Without Temp Variable

a=a+b
b=a-b
a=a-b
print(a,b)